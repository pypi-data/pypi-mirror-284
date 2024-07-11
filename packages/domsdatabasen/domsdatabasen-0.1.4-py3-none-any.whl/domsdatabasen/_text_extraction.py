"""Code to read text from PDFs obtained from domsdatabasen.dk."""

import re
import tempfile
from logging import getLogger
from pathlib import Path
from typing import Any, Dict, List, Tuple, Union

import cv2
import easyocr
import numpy as np
import skimage
import torch
from img2table.document import Image as TableImage
from img2table.tables.objects.extraction import ExtractedTable, TableCell
from omegaconf import DictConfig
from pdf2image import convert_from_path
from pypdf import PdfReader
from skimage import measure
from skimage.filters import rank
from skimage.measure._regionprops import RegionProperties
from tika import parser
from tqdm import tqdm

from ._constants import (
    BOX_HEIGHT_LOWER_BOUND,
    DPI,
    LENGTH_SIX_LETTERS,
    NEW_LINE_PIXEL_LENGTH,
    TAB_PIXEL_LENGTH,
)

logger = getLogger(__name__)


class PDFTextReader:
    """Class for reading text from PDFs obtained from domsdatabasen.dk.

    Args:
        config (DictConfig):
            Config file

    Attributes:
        config (DictConfig):
            Config file
        reader (easyocr.Reader):
            Easyocr reader
    """

    def __init__(self, config: DictConfig):
        """Initialize PDFTextReader."""
        self.config = config
        self.reader = easyocr.Reader(["da"], gpu=torch.cuda.is_available())

    def extract_text(self, pdf_path: Path) -> dict[Any, Any]:
        """Extracts text from a PDF using easyocr or pypdf.

        Some text is anonymized with boxes, and some text
        is anonymized with underlines.
        This function tries to find these anonymization,
        read the anonymized text,
        and then remove the anonymized text from the image before
        reading the rest of the text with easyocr.
        If a page has no anonymization or tables,
        the text is read with pypdf.

        Args:
            pdf_path (Path):
                Path to PDF.

        Returns:
            pdf_data (dict):
                Data about PDF - which anonymization that is used,
                and text + extraction method for each page.
        """
        pdf_reader = PdfReader(pdf_path)

        images = self._get_images(pdf_path=pdf_path)
        pages: Dict[str, Dict[str, str]] = {}

        # I have not seen a single PDF that uses both methods.
        # Try both methods until it is known which method is used.
        # Then use that method for the rest of the PDF.
        box_anonymization = True
        underline_anonymization = True

        for i, image in tqdm(enumerate(images), desc="Reading PDF", total=len(images)):
            page_num = str(i + 1)
            logger.info(f"Reading page {page_num}")

            pages[page_num] = {
                "text": "",
                "extraction_method": "",
            }

            anonymized_boxes = []
            anonymized_boxes_underlines = []
            underlines = []
            table_boxes = []

            if i == 0:
                image = self._remove_logo(image=image)

            if box_anonymization:
                anonymized_boxes = self._extract_anonymized_boxes(image=image)

                # If box anonymization is used, then
                # don't try to find underline anonymization.
                if anonymized_boxes:
                    underline_anonymization = False

            if underline_anonymization:
                (
                    anonymized_boxes_underlines,
                    underlines,
                ) = self._extract_underline_anonymization_boxes(image=image)

                # If underlines anonymization is used, then
                # don't try to find box anonymization.
                if anonymized_boxes_underlines:
                    box_anonymization = False

            # Use a pdf reader if no signs of anonymization are found.
            if not anonymized_boxes and not anonymized_boxes_underlines:
                tables = self._find_tables(image=image.copy(), read_tables=False)
                if not tables:
                    current_page = pdf_reader.pages[i]
                    page_text = current_page.extract_text()
                    pages[page_num]["text"] = page_text.strip()
                    pages[page_num]["extraction_method"] = "pypdf"
                    # Continue to next page.
                    continue

            all_anonymized_boxes = anonymized_boxes + anonymized_boxes_underlines

            image_processed = self._process_image(
                image=image.copy(),
                anonymized_boxes=all_anonymized_boxes,
                underlines=underlines,
            )

            image_processed_inverted = cv2.bitwise_not(image_processed)
            table_boxes = self._find_tables(
                image=image_processed_inverted, read_tables=True
            )

            image_final = self._remove_tables(
                image=image_processed, table_boxes=table_boxes
            )

            main_text_boxes = self._get_main_text_boxes(image=image_final)

            # Merge all boxes and get text from them.
            all_boxes = main_text_boxes + all_anonymized_boxes + table_boxes
            page_text = self._get_text_from_boxes(boxes=all_boxes)

            pages[page_num]["text"] = page_text.strip()
            pages[page_num]["extraction_method"] = "easyocr"

        pdf_data = self._pdf_data(
            pages=pages,
            box_anonymization=box_anonymization,
            underline_anonymization=underline_anonymization,
            pdf_path=pdf_path,
        )
        return pdf_data

    def _pdf_data(
        self,
        pages: Dict[str, Dict[str, str]],
        box_anonymization: bool,
        underline_anonymization: bool,
        pdf_path: Path,
    ) -> dict[str, Union[str, Dict[str, str]]]:
        """Get data about PDF.

        Args:
            pages (dict):
                Pages with text and extraction method.
            box_anonymization (bool):
                True if anonymized boxes are used in PDF. False otherwise.
            underline_anonymization (bool):
                True if underlines are used in PDF. False otherwise.
            pdf_path (Path):
                Path to PDF.

        Returns:
            pdf_data (dict):
                Data about PDF.
        """
        pdf_data: Dict[str, Any] = {}
        anonymization_method = self._anonymization_used(
            box_anonymization=box_anonymization,
            underline_anonymization=underline_anonymization,
        )
        pdf_data["anonymization_method"] = anonymization_method
        pdf_data["pages"] = pages
        pdf_data["text_tika"] = self._read_text_with_tika(pdf_path=str(pdf_path))
        return pdf_data

    def _anonymization_used(
        self, box_anonymization: bool, underline_anonymization: bool
    ) -> str:
        """Return anonymization method used in PDF.

        Args:
            box_anonymization (bool):
                True if anonymized boxes are used in PDF. False otherwise.
            underline_anonymization (bool):
                True if underlines are used in PDF. False otherwise.

        Returns:
            str:
                Anonymization method used in PDF.
        """
        # Both will only be true, if not any of
        # the anonymization methods are used.
        if box_anonymization and underline_anonymization:
            return self.config.anon_method.none
        elif box_anonymization:
            return self.config.anon_method.box
        else:
            return self.config.anon_method.underline

    def _get_main_text_boxes(self, image: np.ndarray) -> List[dict]:
        """Read main text of page.

        Args:
            image (np.ndarray):
                Image to read text from.

        Returns:
            main_text_boxes (List[dict]):
                List of boxes with coordinates and text.
        """
        result = self.reader.readtext(image=image)

        main_text_boxes = [self._change_box_format(easyocr_box=box) for box in result]
        return main_text_boxes

    def _extract_anonymized_boxes(self, image: np.ndarray) -> List[dict]:
        """Extract anonymized boxes from image.

        Find and read text from anonymized boxes in image.

        Args:
            image (np.ndarray):
                Image to find anonymized boxes in.

        Returns:
            anonymized_boxes_with_text (List[dict]):
                List of anonymized boxes with coordinates and text.
        """
        anonymized_boxes = self._find_anonymized_boxes(image=image.copy())

        anonymized_boxes_with_text = [
            self._read_text_from_anonymized_box(
                image=image.copy(),
                anonymized_box=anonymized_box,
                invert=self.config.process.invert_find_anonymized_boxes,
            )
            for anonymized_box in anonymized_boxes
        ]

        return anonymized_boxes_with_text

    def _extract_underline_anonymization_boxes(self, image: np.ndarray) -> Tuple:
        """Extract boxes from underline anonymization.

        Find underlines, make boxes above them, and read text from the boxes.

        Args:
            image (np.ndarray):
                Image to find underline anonymization in.

        Returns:
            anonymized_boxes_underlines_ (List[dict]):
                List of boxes with coordinates and text.
            underlines (List[tuple]):
                List of underlines with coordinates.
        """
        anonymized_boxes_underlines, underlines = self._line_anonymization_to_boxes(
            image=image.copy(),
        )

        anonymized_boxes_underlines_ = [
            self._read_text_from_anonymized_box(
                image.copy(),
                box,
                invert=self.config.process.invert_find_underline_anonymizations,
            )
            for box in anonymized_boxes_underlines
        ]
        return anonymized_boxes_underlines_, underlines

    def _get_images(self, pdf_path: Path) -> List[np.ndarray]:
        """Get images from PDF.

        Returns all images from PDF, except if debugging a single page.
        In that case page self.config.process.page_number is returned.

        Args:
            pdf_path (Path):
                Path to PDF.

        Returns:
            images (List[np.ndarray]):
                List of images from PDF.
        """
        if self.config.process.page_number:
            # Used for debugging a single page
            images = list(
                map(
                    np.array,
                    convert_from_path(
                        pdf_path,
                        dpi=DPI,
                        first_page=self.config.process.page_number,
                        last_page=self.config.process.page_number,
                    ),
                )
            )
        else:
            images = list(map(np.array, convert_from_path(pdf_path=pdf_path, dpi=DPI)))

        # Grayscale
        images = list(
            map(lambda image: cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), images)
        )
        return images

    def _find_tables(self, image: np.ndarray, read_tables: bool = False) -> List[dict]:
        """Extract tables from the image.

        Args:
            image (np.ndarray):
                Image to find tables in.
                The tables in the image should have black borders.
                E.g. the image should not be inverted.
            read_tables (bool):
                True if tables should be read. False otherwise.

        Returns:
            table_boxes (List[dict]):
                List of tables with coordinates and text.
        """
        with tempfile.NamedTemporaryFile(suffix=".png") as tmp:
            cv2.imwrite(tmp.name, image)
            table_image = TableImage(src=tmp.name, detect_rotation=False)
            try:
                tables = table_image.extract_tables()
            except Exception as e:
                logger.error(f"Error extracting tables: {e}")
                return []

        if not read_tables:
            return tables

        for table in tables:
            self._read_table(table=table, image=image)

        table_boxes = [self._table_to_box_format(table=table) for table in tables]

        return table_boxes

    def _process_before_table_search(self, image: np.ndarray) -> np.ndarray:
        """Process image before searching for tables.

        Keep only vertical and horizontal lines.

        Args:
            image (np.ndarray):
                Image to process.

        Returns:
            image_processed (np.ndarray):
                Processed image to search for tables in.
        """
        inverted = cv2.bitwise_not(image)

        t = self.config.process.threshold_binarize_process_before_table_search
        binary = self._binarize(image=inverted, threshold=t, val_min=0, val_max=255)

        open_v = cv2.morphologyEx(binary, cv2.MORPH_OPEN, np.ones((10, 1)))
        open_h = cv2.morphologyEx(binary, cv2.MORPH_OPEN, np.ones((1, 20)))
        combined = cv2.bitwise_or(open_v, open_h)

        invert_back = cv2.bitwise_not(combined)

        image_processed = invert_back
        return image_processed

    def _get_coordinates(
        self, table_or_cell: List[Union[ExtractedTable, TableCell]]
    ) -> Tuple[int, int, int, int]:
        """Get coordinates of table or cell.

        Args:
            table_or_cell (Union[ExtractedTable, TableCell]):
                Table or cell to get coordinates from.

        Returns:
            (tuple):
                Coordinates of table or cell.
        """
        assert hasattr(table_or_cell, "bbox"), "table_or_cell must have attribute bbox"

        row_min, col_min, row_max, col_max = (
            table_or_cell.bbox.y1,
            table_or_cell.bbox.x1,
            table_or_cell.bbox.y2,
            table_or_cell.bbox.x2,
        )
        return row_min, col_min, row_max, col_max

    def _table_to_box_format(self, table: ExtractedTable) -> dict:
        """Convert table to box format.

        Args:
            table (ExtractedTable):
                Table to convert.

        Returns:
            table_box (dict):
                Table in box format.
        """
        row_min, col_min, row_max, col_max = self._get_coordinates(table_or_cell=table)

        table_string = self._table_string(table=table)

        table_box = {
            "coordinates": (row_min, col_min, row_max, col_max),
            "text": table_string,
            "shape": table.df.shape,
        }
        return table_box

    def _table_string(self, table: ExtractedTable) -> str:
        """Convert table to string.

        Args:
            table (ExtractedTable):
                Table to convert.

        Returns:
            table_string (str):
                Table as string (markdown format).
        """
        df = table.df
        df.columns = ["" for _ in range(len(df.columns))]

        table_string = df.to_markdown(index=False, headers=[])
        table_string = "<table>\n" + table_string + "\n</table>"
        return table_string

    def _read_table(self, table: ExtractedTable, image: np.ndarray) -> None:
        """Read text in table.

        Args:
            table (ExtractedTable):
                Table to read text from.
            image (np.ndarray):
                Image that the table is extracted from.
        """
        for row in table.content.values():
            for cell in row:
                self._read_text_from_cell(cell, image)

    def _read_text_from_cell(self, cell: TableCell, image: np.ndarray) -> None:
        """Read text from cell with easyocr.

        Args:
            cell (TableCell):
                Cell to read text from.
            image (np.ndarray):
                Image that the cell is extracted from.
        """
        inverted = cv2.bitwise_not(image)
        cell_box = self._cell_to_box(cell)
        crop = self._box_to_crop(box=cell_box, image=inverted)
        if self._empty_image(
            image=crop,
            binarize_threshold=self.config.process.threshold_binarize_empty_box,
        ):
            cell.value = ""
            return

        binary = self._binarize(
            image=crop, threshold=self.config.process.threshold_binarize_empty_box
        )
        split_indices = self._multiple_lines(binary=binary)
        if not split_indices:
            cell_boxes = [cell_box]
        else:
            cell_boxes = self._split_cell_box(
                cell_box=cell_box, split_indices=split_indices
            )

        all_text = ""
        for cell_box_ in cell_boxes:
            crop = self._box_to_crop(box=cell_box_, image=inverted)
            if self._empty_image(
                image=crop,
                binarize_threshold=self.config.process.threshold_binarize_empty_box,
            ):
                continue

            crop_cleaned = self._remove_boundary_noise(
                crop=crop,
                binary_threshold=self.config.process.threshold_binarize_empty_box,
            )
            if self._empty_image(
                image=crop_cleaned,
                binarize_threshold=self.config.process.threshold_binarize_empty_box,
            ):
                continue

            crops_to_read = self._process_crop_before_read(
                crop=crop_cleaned,
                binary_threshold=self.config.process.threshold_binarize_empty_box,
                refine_padding=self.config.process.cell_box_crop_padding,
                cell=True,
            )

            text = self._read_text_from_crop(crops=crops_to_read, cell=True)
            if all_text and all_text[-1] == "-":
                all_text = all_text[:-1]
                sep = ""
            else:
                sep = " "
            all_text += f"{sep}{text}"

        cell.value = all_text

    def _empty_image(self, image: np.ndarray, binarize_threshold: int) -> bool:
        """Determine if image is empty.

        Args:
            image (np.ndarray):
                Image to determine if is empty.
            binarize_threshold (int):
                Threshold to binarize image with.

        Returns:
            bool:
                True if image is empty. False otherwise.
        """
        binary = self._binarize(image=image, threshold=binarize_threshold)
        return binary.sum() == 0

    def _read_text(self, crop_refined: np.ndarray) -> str:
        """Read text from subimage of cell.

        Args:
            crop_refined (np.ndarray):
                Subimage of cell.

        Returns:
            text (str):
                Text from subimage of cell.
        """
        result = self.reader.readtext(image=crop_refined)
        if not result:
            text = ""
        else:
            # Sort w.r.t x-coordinate
            result = self._sort_result_by_x(result=result)

            text = result[0][1]
            for box in result[1:]:
                box_text = box[1]
                sep = "" if text[-1] == "-" else " "
                text += f"{sep}{box_text}"
        return f"{text}\n"

    def _sort_result_by_x(self, result: List[tuple]) -> List[tuple]:
        """Sort result from easyocr by x-coordinate.

        Args:
            result (List[tuple]):
                Result from easyocr using `reader.readtext()`.

        Returns:
            result (List[tuple]):
                Result sorted by x-coordinate.
        """
        return sorted(result, key=lambda x: x[0][0][0])

    def _split_cell_box(
        self, cell_box: TableCell, split_indices: List[int]
    ) -> List[dict]:
        """Split cell box into multiple cell boxes.

        Split each cell box into multiple cell boxes, one for each line.

        Args:
            cell_box (TableCell):
                Cell box to split.
            split_indices (List[int]):
                Indices to split cell box at.

        Returns:
            cell_boxes (List[dict]):
                List of cell boxes.
        """
        row_min, col_min, row_max, col_max = cell_box["coordinates"]

        cell_boxes = []

        # First box.
        first_box = {
            "coordinates": (row_min, col_min, row_min + split_indices[0], col_max)
        }
        cell_boxes.append(first_box)

        # Boxes in between first and last.
        if len(split_indices) > 1:
            for split_index_1, split_index_2 in zip(
                split_indices[:-1], split_indices[1:]
            ):
                cell_box_ = {
                    "coordinates": (
                        row_min + split_index_1 + 1,
                        col_min,
                        row_min + split_index_2,
                        col_max,
                    )
                }
                cell_boxes.append(cell_box_)

        # Last box.
        last_box = {
            "coordinates": (row_min + split_indices[-1] + 1, col_min, row_max, col_max)
        }
        cell_boxes.append(last_box)

        return cell_boxes

    def _cell_to_box(self, cell: TableCell) -> dict:
        """Convert cell to box format.

        Args:
            cell (TableCell):
                Cell to convert.

        Returns:
            cell_box (dict):
                Cell in box format.
        """
        p = self.config.process.remove_cell_border
        row_min, col_min, row_max, col_max = self._get_coordinates(table_or_cell=cell)
        cell_box = {"coordinates": (row_min + p, col_min + p, row_max - p, col_max - p)}
        return cell_box

    def _multiple_lines(self, binary: np.ndarray) -> List[int]:
        """Used to detect multiple lines in a cell.

        Args:
            binary (np.ndarray):
                Binary image of cell.

        Returns:
            split_indices (List[int]):
                Row indices to split cell at.
        """
        rows, _ = np.where(binary > 0)
        diffs = np.diff(rows)

        # Locate where the there are large gaps without text.
        jump_indices = np.where(
            diffs > self.config.process.cell_multiple_lines_gap_threshold
        )[0]
        split_indices = []
        for jump_idx in jump_indices:
            top = rows[jump_idx]
            bottom = rows[jump_idx + 1]
            split_index = (top + bottom) // 2
            split_indices.append(split_index)
        return split_indices

    @staticmethod
    def _get_blobs(binary: np.ndarray, sort_function=None) -> List[RegionProperties]:
        """Get blobs from binary image.

        Find all blobs in a binary image, and return the
        blobs sorted by area of its bounding box.

        Args:
            binary (np.ndarray):
                Binary image
            sort_function (function):
                Function to sort blobs by.

        Returns:
            blobs (list):
                List of blobs sorted by area of its bounding box.
        """
        if sort_function is None:

            def sort_function(blob):
                return blob.area_bbox

        labels = measure.label(label_image=binary, connectivity=1)
        blobs = measure.regionprops(label_image=labels)
        blobs = sorted(blobs, key=sort_function, reverse=True)
        return blobs

    def _line_anonymization_to_boxes(self, image: np.ndarray) -> tuple:
        """Finds all underlines and makes anonymized boxes above them.

        Args:
            image (np.ndarray):
                Image to find anonymized boxes in.

        Returns:
            anonymized_boxes (List[dict]):
                List of anonymized boxes with coordinates
                (boxes above found underlines).
            underlines (List[tuple]):
                List of underlines with coordinates
                (will later be used to remove the underlines from the image).
        """
        inverted = cv2.bitwise_not(image)
        binary = self._binarize(
            image=inverted,
            threshold=self.config.process.threshold_binarize_line_anonymization,
            val_min=0,
            val_max=255,
        )

        blobs = self._get_blobs(binary=binary, sort_function=self._blob_length)

        anonymized_boxes: List[dict] = []
        underlines = []
        for blob in blobs:
            if self._blob_length(blob=blob) < self.config.process.underline_length_min:
                break
            underline = self._extract_underline(blob=blob)
            if not underline:
                continue

            row_min, col_min, _, col_max = underline

            expand = self.config.process.underline_box_expand
            box_row_min = row_min - self.config.process.underline_box_height
            box_row_max = row_min - 1  # Just above underline
            box_col_min = col_min - expand
            box_col_max = col_max + expand

            anonymized_box = {
                "coordinates": [box_row_min, box_col_min, box_row_max, box_col_max],
                "origin": self.config.process.origin_underline,
            }

            crop = inverted[box_row_min:box_row_max, box_col_min:box_col_max]
            if crop.sum() == 0:
                # Box is empty
                continue

            box_is_duplicate = any(
                self._too_much_overlap(box_1=anonymized_box, box_2=box)
                for box in anonymized_boxes
            )
            if not box_is_duplicate:
                anonymized_boxes.append(anonymized_box)
                underlines.append(underline)

        return anonymized_boxes, underlines

    def _extract_underline(self, blob: RegionProperties) -> Tuple:
        """Extract underline from blob.

        Blob might be an underline. If it is, then return the underline.
        Else, return empty tuple.

        Args:
            blob (RegionProperties):
                Blob to extract underline from.

        Returns:
            underline (tuple):
                Underline with coordinates, empty
                tuple if blob is not an underline.
        """
        rows, cols = blob.coords.transpose()
        col_min = cols.min()
        col_max = cols.max()

        rows_at_col_min = rows[cols == col_min]
        rows_at_col_max = rows[cols == col_max]

        if (
            not len(rows_at_col_min) == len(rows_at_col_max)
            or not (rows_at_col_min == rows_at_col_max).all()
        ):
            return ()

        row_min = rows_at_col_min.min()
        row_max = rows_at_col_min.max()

        def _perfect_rectangle():
            """Perfect rectangle is a rectangle where all pixels are filled."""
            n_pixels = sum(len(cols[rows == row]) for row in rows_at_col_min)
            x = col_max - col_min + 1
            y = row_max - row_min + 1
            if x * y == n_pixels:
                return True

        if not _perfect_rectangle():
            return ()

        # Bounds for height of underline.
        lb, ub = (
            self.config.process.underline_height_lower_bound,
            self.config.process.underline_height_upper_bound,
        )
        height = row_max - row_min + 1
        if not lb < height < ub:
            return ()

        # +1 becauses box coordinates should be exclusive,
        # e.g. [row_min, row_max)
        return row_min, col_min, row_max + 1, col_max + 1

    @staticmethod
    def _blob_length(blob: RegionProperties) -> int:
        """Number of pixels in the bottom row of the blob.

        Args:
            blob (RegionProperties):
                Blob to get length of.

        Returns:
            int:
                Number of pixels in the bottom row of the blob.
        """
        _, cols = blob.coords.transpose()
        col_min = cols.min()
        col_max = cols.max()
        length = col_max - col_min + 1
        return length

    def _too_much_overlap(self, box_1: dict, box_2: dict) -> bool:
        """Used to determine if two boxes overlap too much.

        For example case 1586 page 4 has an anonymization with two underlines,
        which results in two boxes overlapping. This function is used
        to determine if the boxes overlap too much.

        Args:
            box_1 (dict):
                Anonymized box with coordinates.
            box_2 (dict):
                Anonymized box with coordinates.

        Returns:
            bool:
                True if boxes overlap too much. False otherwise.
        """
        return (
            self._intersection_over_union(box_1=box_1, box_2=box_2)
            > self.config.process.iou_overlap_threshold
        )

    def _intersection_over_union(self, box_1: dict, box_2: dict) -> float:
        """Calculates intersection over union (IoU) between two boxes.

        Args:
            box_1 (dict):
                Anonymized box with coordinates.
            box_2 (dict):
                Anonymized box with coordinates.

        Returns:
            float:
                Intersection over union (IoU) between two boxes.
        """
        return self._intersection(box_1=box_1, box_2=box_2) / self._union(
            box_1=box_1, box_2=box_2
        )

    @staticmethod
    def _intersection(box_1: dict, box_2: dict) -> float:
        """Calculates intersection between two boxes.

        Args:
            box_1 (dict):
                Anonymized box with coordinates.
            box_2 (dict):
                Anonymized box with coordinates.

        Returns:
            float:
                Intersection between two boxes.
        """
        row_min1, col_min1, row_max1, col_max1 = box_1["coordinates"]
        row_min2, col_min2, row_max2, col_max2 = box_2["coordinates"]
        y_side_length = min(row_max1, row_max2) - max(row_min1, row_min2)
        x_side_length = min(col_max1, col_max2) - max(col_min1, col_min2)
        return (
            y_side_length * x_side_length
            if y_side_length > 0 and x_side_length > 0
            else 0
        )

    def _union(self, box_1: dict, box_2: dict) -> float:
        """Calculates the area of the union between two boxes.

        Args:
            box_1 (dict):
                Anonymized box with coordinates.
            box_2 (dict):
                Anonymized box with coordinates.

        Returns:
            float:
                area of the union between the two boxes.
        """
        area_1 = self._area(box=box_1)
        area_2 = self._area(box=box_2)
        return area_1 + area_2 - self._intersection(box_1=box_1, box_2=box_2)

    @staticmethod
    def _area(box: dict) -> int:
        """Calculates the area of a box.

        Args:
            box (dict):
                Anonymized box with coordinates.

        Returns:
            int:
                Area of the box.
        """
        row_min, col_min, row_max, col_max = box["coordinates"]
        return (row_max - row_min) * (col_max - col_min)

    def _remove_logo(self, image: np.ndarray) -> np.ndarray:
        """Removes logo from image.

        For many PDFs, there is a logo in the top of the first page.

        Args:
            image (np.ndarray):
                Image to remove logo from.

        Returns:
            np.ndarray:
                Image with logo removed.
        """
        r = self.config.process.page_from_top_to_this_row
        page_top = image[:r, :]
        page_top_binary = self._process_top_page(page_top=page_top)

        blobs = self._get_blobs(binary=page_top_binary)
        if blobs:
            blob_largest = blobs[0]
            # If largest blob is too large, then we are probably dealing with a logo.
            if blob_largest.area_bbox > self.config.process.logo_bbox_area_threshold:
                # Remove logo
                row_min, col_min, row_max, col_max = blob_largest.bbox
                page_top[row_min:row_max, col_min:col_max] = 255
                image[:r, :] = page_top

        return image

    def _process_top_page(self, page_top: np.ndarray) -> np.ndarray:
        """Processes logo for blob detection.

        Args:
            page_top (np.ndarray):
                Top part of page.

        Returns:
            np.ndarray:
                Processed top part.
        """
        logo_binary = self._binarize(
            image=page_top,
            threshold=self.config.process.threshold_binarize_top_page,
            val_min=0,
            val_max=255,
        )
        inverted = cv2.bitwise_not(logo_binary)
        return inverted

    def _on_same_line(self, y: int, y_prev: int) -> bool:
        """Determine if two bounding boxes are on the same line.

        Args:
            y (int):
                y coordinate of top left corner of current bounding box.
            y_prev (int):
                y coordinate of top left corner of previous bounding box.
            max_y_difference (int):
                Maximum difference between y coordinates of two
                bounding boxes on the same line.

        Returns:
            bool:
                True if the two bounding boxes are on the same line. False otherwise.
        """
        return abs(y - y_prev) < self.config.process.max_y_difference

    def _process_image(
        self, image: np.ndarray, anonymized_boxes: List[dict], underlines: List[tuple]
    ) -> np.ndarray:
        """Prepare image for easyocr to read the main text (all non-anonymized text).

        Removes all anonymized boxes and underlines from the image,
        and then performs some image processing to make the text easier to read.

        Args:
            image (np.ndarray):
                Image to be processed.
            anonymized_boxes (List[dict]):
                List of anonymized boxes with coordinates.
            underlines (List[tuple]):
                List of underlines with coordinates.

        Returns:
            np.ndarray:
                Processed image.
        """
        # For the anonymized boxes there already are black boxes,
        # but we will remove the text inside them, by making the text black.
        # The boxes made above underlines is included in the anonymized boxes.
        # For these there are no boxes above them, but only text,
        # but that text is simply removed by making a black box.
        image = self._remove_text_in_anonymized_boxes(
            image=image, anonymized_boxes=anonymized_boxes
        )

        image = self._draw_bbox_for_underlines(image=image, underlines=underlines)

        # Invert such that it is white text on black background.
        inverted = cv2.bitwise_not(image)

        # Image has been inverted, such that it is white text on black background.
        # However this also means that the boxes and underlines currently are white.
        # We want to remove them entirely. We do this using flood fill.
        filled = inverted.copy()

        filled[filled < 5] = 0
        opened = cv2.morphologyEx(filled, cv2.MORPH_OPEN, np.ones((30, 30)))
        opened_binary = self._binarize(
            image=opened,
            threshold=self.config.process.threshold_binarize_process_image,
            val_min=0,
            val_max=255,
        )
        opened_binary_dilated = cv2.dilate(opened_binary, np.ones((3, 3)))

        for anonymized_box in anonymized_boxes:
            row_min, col_min, row_max, col_max = anonymized_box["coordinates"]

            center = (row_min + row_max) // 2, (col_min + col_max) // 2

            if opened[center] != 255:
                # Box is already removed, supposedly because
                # it overlaps with a previous box.
                continue

            mask = skimage.segmentation.flood(
                image=opened_binary_dilated,
                seed_point=center,
            )
            filled[mask] = 0

        pad = self.config.process.underline_remove_pad
        for underline in underlines:
            row_min, col_min, row_max, col_max = underline
            # Remove underline
            filled[row_min - pad : row_max + pad, col_min - pad : col_max + pad] = 0

        # Increase size of letters slightly
        dilated = cv2.dilate(filled, np.ones((2, 2)))
        image_processed = dilated

        return image_processed

    def _draw_bbox_for_underlines(
        self, image: np.ndarray, underlines: List[tuple]
    ) -> np.ndarray:
        """Draws bounding boxes for underlines.

        Args:
            image (np.ndarray):
                Image to draw bounding boxes on.
            underlines (List[tuple]):
                List of underlines with coordinates.

        Returns:
            np.ndarray:
                Image with bounding boxes drawn on the underlines.
        """
        for underline in underlines:
            row_min, col_min, row_max, col_max = underline
            image[row_min : row_max + 1, col_min : col_max + 1] = 0
        return image

    def _remove_text_in_anonymized_boxes(
        self, image: np.ndarray, anonymized_boxes: List[dict]
    ) -> np.ndarray:
        """Removes text in anonymized boxes.

        Args:
            image (np.ndarray):
                Image where boxes are found in.
            anonymized_boxes (List[dict]):
                List of anonymized boxes with coordinates.
        """
        for box in anonymized_boxes:
            row_min, col_min, row_max, col_max = box["coordinates"]
            image[row_min:row_max, col_min:col_max] = 0
        return image

    def _remove_tables(self, image: np.ndarray, table_boxes: List[dict]) -> np.ndarray:
        """Removes tables from image.

        Args:
            image (np.ndarray):
                Image to remove tables from.
            table_boxes (List[dict]):
                List of tables with coordinates.

        Returns:
            np.ndarray:
                Image with tables removed.
        """
        for table_box in table_boxes:
            row_min, col_min, row_max, col_max = table_box["coordinates"]

            p = self.config.process.remove_table_border
            image[row_min - p : row_max + p, col_min - p : col_max + p] = 0
        return image

    def _to_box_format(self, cell: TableCell):
        """Convert cell to box format.

        Args:
            cell (TableCell):
                Cell to convert.

        Returns:
            cell_box (dict):
                Cell in box format.
        """
        row_min, col_min, row_max, col_max = self._get_coordinates(table_or_cell=cell)
        s = self.config.process.cell_box_shrink
        # Better way to remove white border?
        # Flood fill if border is white?
        # Might be possible to use `_remove_boundary_noise`
        # Keep code as it is for now, as long as
        # no problems are encountered.
        cell_box = {"coordinates": (row_min + s, col_min + s, row_max - s, col_max - s)}
        return cell_box

    def _get_text_from_boxes(self, boxes: List[dict]) -> str:
        """Get text from boxes.

        Sorts all boxes w.r.t how a person would read the text,
        and then joins the text together.

        Args:
            boxes (List[dict]):
                List of boxes with coordinates and text
            max_y_difference (int):
                Maximum difference between y coordinates of
                two bounding boxes on the same line.

        Returns:
            page_text (str):
                Text from current page.
        """
        if not boxes:
            # Empty page supposedly
            return ""

        # Remove multiple spaces
        boxes = [self._remove_multiple_spaces(box=box) for box in boxes]

        # Sort w.r.t y coordinate.
        boxes_y_sorted = sorted(boxes, key=lambda box: self._middle_y_cordinate(box))

        # Group bounding boxes that are on the same line.
        # E.g. the variable `lines`` will be a list of lists, where each list contains
        # the bounding boxes for a given line of text in the pdf.
        # The variable `max_y_difference` is used to determine if two bounding boxes
        # are on the same line. E.g. if the difference between the y coordinates of
        # two bounding boxes is less than `max_y_difference`,
        # then the two bounding boxes are said to be on the same line.
        current_line = [boxes_y_sorted[0]]
        lines = [current_line]
        ys = []
        for i in range(1, len(boxes_y_sorted)):
            box = boxes_y_sorted[i]
            box_prev = boxes_y_sorted[i - 1]
            y = self._middle_y_cordinate(box)
            y_prev = self._middle_y_cordinate(box_prev)
            ys.append(y_prev)
            if self._on_same_line(y, y_prev):
                # Box is on current line.
                lines[-1].append(box)
            else:
                # Box is on a new line.
                new_line = [box]
                lines.append(new_line)

        # Now sort each line w.r.t x coordinate.
        # The lines should as a result be sorted w.r.t how a text is read.
        for i, line in enumerate(lines):
            line_ = sorted(line, key=lambda box: self._left_x_cordinate(box))
            line_ = self._removed_unwanted_boxes(line=line_)
            lines[i] = line_

        # Ignore unwanted lines
        # Currently only footnotes are ignored.
        # Might want to add more conditions later.
        # For example, ignore page numbers.
        lines_ = [line for line in lines if not self._ignore_line(line)]

        page_text = self._lines_to_page_text(lines=lines_)

        return page_text

    def _lines_to_page_text(self, lines: List[List[dict]]) -> str:
        """Convert lines to page text.

        Args:
            lines (List[List[dict]]):
                List of lines, where each line is a list of boxes.

        Returns:
            page_text (str):
                Text from current page.
        """
        if not lines:
            return ""
        text_first_line = self._join_line(line=lines[0])
        page_text = text_first_line

        for i in range(1, len(lines)):
            line = lines[i]
            line_prev = lines[i - 1]
            distance = self._distance_between_lines(line_1=line, line_2=line_prev)
            n_newlines = distance // NEW_LINE_PIXEL_LENGTH or 1
            text_line = self._join_line(line=line)
            page_text += "\n" * n_newlines + text_line
        return page_text

    def _distance_between_lines(self, line_1: List[dict], line_2: List[dict]) -> int:
        """Distance between two lines.

        Args:
            line_1 (List[dict]):
                List of boxes on first line.
            line_2 (List[dict]):
                List of boxes on second line.

        Returns:
            int:
                Distance between two lines.
        """
        box = line_1[0]
        box_prev = line_2[0]
        return int(self._box_distance_horizontal(box_1=box, box_2=box_prev))

    def _box_distance_horizontal(self, box_1: dict, box_2: dict) -> int:
        """Horizontal distance between two boxes.

        Args:
            box_1 (dict):
                Anonymized box with coordinates.
            box_2 (dict):
                Anonymized box with coordinates.

        Returns:
            int:
                Horizontal distance between two boxes.
        """
        mid_1 = self._middle_row_cordinate(box_1)
        mid_2 = self._middle_row_cordinate(box_2)
        return abs(mid_1 - mid_2)

    def _middle_row_cordinate(self, box: dict) -> int:
        """Middle row coordinate of box.

        Args:
            box (dict):
                Anonymized box with coordinates.

        Returns:
            int:
                Middle row coordinate of box.
        """
        row_min, _, row_max, _ = box["coordinates"]
        return (row_min + row_max) // 2

    def _remove_multiple_spaces(self, box: dict) -> dict:
        """Remove multiple spaces from box text.

        Args:
            box (dict):
                Anonymized box with text.

        Returns:
            box (dict):
                Anonymized box with text, where multiple spaces are removed.
        """
        text_cleaned = re.sub(r" +", " ", box["text"])
        box["text"] = text_cleaned
        return box

    def _removed_unwanted_boxes(self, line: List[dict]) -> List[dict]:
        """Remove unwanted boxes from line.

        Remove boxes that are not part of the main text.
        For example, there might be an info box to the right of the main text.
        We want to remove this info box.

        Args:
            line (List[dict]):
                List of boxes on the line.

        Returns:
            line (List[dict]):
                List of boxes on the line with unwanted boxes removed.
        """
        # Get index of first box that contains text.
        i = 0
        while i < len(line):
            box = line[i]
            if box["text"]:
                break
            i += 1
        if i == len(line):
            # No box contains text.
            return []

        box_first = line[i]
        col_start = box_first["coordinates"][1]
        if col_start > self.config.process.line_start_ignore_col:
            return []

        line_ = [box_first]
        for j in range(i + 1, len(line)):
            box = line[j]
            box_prev = line[j - 1]
            distance = self._box_distance(box_1=box_prev, box_2=box)
            if distance > 2 * TAB_PIXEL_LENGTH:
                break
            line_.append(box)
        return line_

    def _join_line(self, line: List[dict]) -> str:
        """Join line of boxes together.

        If boxes on a line are far apart, then join the boxes with tabs,
        otherwise join the boxes with spaces.

        Args:
            line (List[dict]):
                List of boxes on the line.

        Returns:
            line_text (str):
                Text from line.
        """
        box_first = line[0]
        line_text = box_first["text"]
        for i in range(1, len(line)):
            box = line[i]
            box_prev = line[i - 1]
            distance = self._box_distance(box_1=box_prev, box_2=box)
            n_tabs = distance // TAB_PIXEL_LENGTH
            sep = "\t" * n_tabs if n_tabs > 0 else " "
            line_text += f"{sep}{box['text']}"
        return line_text

    def _box_distance(self, box_1: dict, box_2: dict) -> int:
        """Distance between two boxes.

        The distance between the right side of box 1 and the left side of box 2.
        Box 1 must be to the left of box 2.

        Args:
            box_1 (dict):
                Anonymized box with coordinates.
            box_2 (dict):
                Anonymized box with coordinates.

        Returns:
            int:
                Distance between two boxes.
        """
        col_start_box_2 = box_2["coordinates"][1]
        col_end_box_1 = box_1["coordinates"][3]
        return int(col_start_box_2 - col_end_box_1)

    def _ignore_line(self, line: List[dict]) -> bool:
        """Checks if line should be ignored.

        We want to ignore lines that are footnotes.
        Might want to add more conditions later.
        For example, ignore page numbers.

        Args:
            line (List[dict]):
                List of boxes on the line.

        Returns:
            bool:
                True if line should be ignored. False otherwise.
        """
        if not line:
            return True
        first_box = line[0]
        ignore = self._is_footnote(first_box)
        return ignore

    def _is_footnote(self, first_box: dict):
        """Checks if line is a footnote.

        If the first box in the line is far to the right and far down,
        then it is probably a footnote.

        Args:
            first_box (dict):
                First box in line.

        Returns:
            bool:
                True if line is a footnote. False otherwise.
        """
        row_min, col_min, row_max, _ = first_box["coordinates"]
        height = row_max - row_min
        return (
            col_min > self.config.process.line_start_ignore_col
            and row_min > self.config.process.line_start_ignore_row
            and height < self.config.process.threshold_footnote_height
        )

    @staticmethod
    def _left_x_cordinate(anonymized_box: dict) -> int:
        """Returns the left x coordinate of a box.

        Used in `_get_text_from_boxes` to sort every line of boxes
        from left to right.

        Args:
            anonymized_box (dict):
                Anonymized box with coordinates.

        Returns:
            int:
                Left x coordinate of box.
        """
        _, col_min, _, _ = anonymized_box["coordinates"]
        return col_min

    @staticmethod
    def _middle_y_cordinate(anonymized_box: dict) -> int:
        """Returns the middle y coordinate of a box.

        Used in `_get_text_from_boxes` to determine if two boxes are on the same line.

        Args:
            anonymized_box (dict):
                Anonymized box with coordinates.

        Returns:
            int:
                Middle y coordinate of box.
        """
        row_min, _, row_max, _ = anonymized_box["coordinates"]
        return (row_min + row_max) // 2

    @staticmethod
    def _change_box_format(easyocr_box: tuple) -> dict:
        """Change box format from easyocr style to anonymized box style.

        Easyocr uses (x, y) format and represents a box by
        its corners. We want to represent a box by its min/max row/col.

        Args:
            easyocr_box (tuple):
                Easyocr box.

        Returns:
            anonymized_box (dict):
                Anonymized box.
        """
        tl, tr, _, bl = easyocr_box[0]
        row_min, col_min, row_max, col_max = tl[1], tl[0], bl[1], tr[0]
        text = easyocr_box[1]
        confidence = easyocr_box[2]
        anonymized_box = {
            "coordinates": (row_min, col_min, row_max, col_max),
            "text": text,
            "confidence": confidence,
        }
        return anonymized_box

    def _read_text_from_anonymized_box(
        self,
        image: np.ndarray,
        anonymized_box: dict,
        invert: bool = False,
    ) -> dict:
        """Read text from anonymized box.

        Args:
            image (np.ndarray):
                Image of the current page.
            anonymized_box (dict):
                Anonymized box with coordinates.
            invert (bool):
                Whether to invert the image or not.
                Easyocr seems to work best with white text on black background.

        Returns:
            anonymized_box (dict):
                Anonymized box with anonymized text.
        """
        # Easyocr seems to work best with white text on black background.
        if invert:
            image = cv2.bitwise_not(image)

        crop = self._box_to_crop(box=anonymized_box, image=image)
        if self._empty_image(
            image=crop,
            binarize_threshold=self.config.process.threshold_binarize_process_crop,
        ):
            anonymized_box["text"] = ""
            return anonymized_box

        crop_cleaned = self._remove_boundary_noise(
            crop=crop.copy(),
            binary_threshold=self.config.process.threshold_binarize_process_crop,
        )
        if self._empty_image(
            image=crop_cleaned,
            binarize_threshold=self.config.process.threshold_binarize_process_crop,
        ):
            anonymized_box["text"] = ""
            return anonymized_box

        crop_refined, anonymized_box_refined = self._refine_box(
            crop=crop_cleaned,
            box=anonymized_box,
            padding=self.config.process.anonymized_box_crop_padding,
            binary_threshold=self.config.process.threshold_binarize_process_crop,
        )
        if (
            crop_refined is False
            or self._empty_image(
                image=crop_refined,
                binarize_threshold=self.config.process.threshold_binarize_process_crop,
            )
            or self._too_small(crop=crop_refined, anonymized_box=anonymized_box_refined)
        ):
            anonymized_box["text"] = ""
            return anonymized_box

        # Make a box for each word in the box
        # I get better results with easyocr using this approach.
        anonymized_boxes = self._split_box(
            crop=crop_refined, anonymized_box=anonymized_box_refined
        )

        if len(anonymized_boxes) == 1:
            crops_to_read = self._process_crop_before_read(
                crop=crop_refined,
                binary_threshold=self.config.process.threshold_binarize_process_crop,
                refine_padding=self.config.process.anonymized_box_crop_padding,
            )
            text = self._read_text_from_crop(crops=crops_to_read)
            anonymized_box["text"] = f"<anonym>{text}</anonym>" if text else ""
            return anonymized_box

        texts = []
        for anonymized_box_ in anonymized_boxes:
            crop = self._box_refined_to_crop(
                box_refined=anonymized_box_, crop_refined=crop_refined
            )
            if self._empty_image(
                image=crop,
                binarize_threshold=self.config.process.threshold_binarize_process_crop,
            ):
                continue

            crops_to_read = self._process_crop_before_read(
                crop=crop,
                binary_threshold=self.config.process.threshold_binarize_process_crop,
                refine_padding=self.config.process.anonymized_box_crop_padding,
            )

            # Read text from image with easyocr
            text = self._read_text_from_crop(crops=crops_to_read)

            texts.append(text)

        text_all = " ".join(text for text in texts if text).strip()

        anonymized_box["text"] = f"<anonym>{text_all}</anonym>" if text_all else ""
        return anonymized_box

    def _too_small(self, crop: np.ndarray, anonymized_box: dict) -> bool:
        """Determine if crop/box is too small to be classified as relevant.

        This is only necessary for anonymized boxes from underlines, as the
        normal anonymized boxes are already filtered by this constraint.

        Args:
            crop (np.ndarray):
                Crop (representing anonymized box) to be processed.
            anonymized_box (dict):
                Anonymized box with coordinates.

        Returns:
            bool:
                True if crop is too small. False otherwise.
        """
        return (
            crop.shape[0] < self.config.process.underline_box_height_min
            and anonymized_box["origin"] == self.config.process.origin_underline
        )

    def _read_text_from_crop(self, crops: List[np.ndarray], cell: bool = False) -> str:
        """Read text from crop.

        Args:
            crops (List[np.ndarray]):
                List of crops to read text from.
            cell (bool):
                Whether crops are cells or not.

        Returns:
            text (str):
                Text from crop.
        """
        if not crops:
            return ""
        results = [self.reader.readtext(crop) for crop in crops]
        if not any(results):
            return ""
        if len(results) > 1:
            result = self._best_result(results=results)
        else:
            result = results[0]

        boxes = [self._change_box_format(box) for box in result]
        boxes = self._remove_inner_boxes(boxes=boxes)
        boxes = self._sort_by_x(boxes=boxes)
        # At this point I only see > 1 box, if eg. a "," is read as "9".
        # Therefore, just use text from first box
        if not cell:
            if len(boxes) > 1:
                if not boxes[1]["text"] == "9":
                    logger.warning("Second box is not 9.")
            box_first = boxes[0]
            text = box_first["text"]
            return text

        text = " ".join(
            [
                box["text"]
                for box in boxes
                if box["confidence"] > self.config.process.threshold_box_confidence
            ]
        )
        return text

    def _best_result(self, results: List[List[tuple]]) -> List[tuple]:
        """Returns the best result.

        The best result is the result with the highest average confidence score.

        Args:
            results (List[List[tuple]]):
                List of results from easyocr.

        Returns:
            result_best (List[tuple]):
                Best result.
        """
        result_best = results[0]
        result_best_score = self._result_score(result=result_best)
        for result in results[1:]:
            result_score = self._result_score(result=result)
            if result_score > result_best_score:
                result_best = result
                result_best_score = result_score
        return result_best

    def _result_score(self, result: List[tuple]) -> float:
        """Calculates the score of a result.

        The score is the average confidence score.

        Args:
            result (List[tuple]):
                Result from easyocr.

        Returns:
            score (float):
                Score of result.
        """
        if len(result) == 0:
            return 0
        n_boxes = len(result)

        # Averge confidence score
        score = sum(box[2] for box in result) * 1 / n_boxes
        return score

    def _sort_by_x(self, boxes: List[dict]) -> List[dict]:
        """Sort boxes by x coordinate.

        Args:
            boxes (List[dict]):
                List of boxes with coordinates.

        Returns:
            List[dict]:
                List of boxes sorted by x coordinate.
        """
        return sorted(boxes, key=lambda box: box["coordinates"][1])

    def _remove_inner_boxes(self, boxes: List[dict]) -> List[dict]:
        """Remove inner boxes.

        If a box is inside another box, then remove the inner box.

        Args:
            boxes (List[dict]):
                List of boxes with coordinates.

        Returns:
            List[dict]:
                List of boxes with inner boxes removed.
        """
        boxes = sorted(boxes, key=lambda box: self._area(box=box), reverse=True)
        boxes_ = [boxes[0]]
        for box in boxes[1:]:
            if not self._inner_box(boxes=boxes_, box=box):
                boxes_.append(box)
        return boxes_

    def _inner_box(self, boxes: List[dict], box: dict) -> bool:
        """Determine if box is inside another box.

        Args:
            boxes (List[dict]):
                List of boxes with coordinates.
            box (dict):
                Box with coordinates.

        Returns:
            bool:
                True if box is inside another box. False otherwise.
        """
        for box_ in boxes:
            if self._inside(box_1=box, box_2=box_):
                return True
        return False

    def _inside(self, box_1: dict, box_2: dict) -> bool:
        """Determine if box_1 is inside box_2.

        Args:
            box_1 (dict):
                Box with coordinates.
            box_2 (dict):
                Box with coordinates.

        Returns:
            bool:
                True if box_1 is inside box_2. False otherwise.
        """
        row_min_1, col_min_1, row_max_1, col_max_1 = box_1["coordinates"]
        row_min_2, col_min_2, row_max_2, col_max_2 = box_2["coordinates"]

        return (
            row_min_2 <= row_min_1
            and col_min_2 <= col_min_1
            and row_max_2 >= row_max_1
            and col_max_2 >= col_max_1
        )

    def _box_refined_to_crop(
        self, box_refined: dict, crop_refined: np.ndarray
    ) -> np.ndarray:
        row_min, col_min, row_max, col_max = box_refined["crop_refined_coordinates"]
        crop = crop_refined[row_min:row_max, col_min:col_max]
        return crop

    def _box_to_crop(self, box: dict, image: np.ndarray) -> dict:
        """Convert box to crop.

        Args:
            box (dict):
                Anonymized box with coordinates.
            image (np.ndarray):
                Image of the current page.

        Returns:
            crop (np.ndarray):
                Crop of image representing the box.
        """
        row_min, col_min, row_max, col_max = box["coordinates"]
        crop = image[row_min:row_max, col_min:col_max]
        return crop

    def _process_crop_before_read(
        self,
        crop: np.ndarray,
        binary_threshold: int,
        refine_padding: int = 0,
        cell: bool = False,
    ) -> np.ndarray:
        """Processes crop before reading text with easyocr.

        I get better results with easyocr using this approach.

        Args:
            crop (np.ndarray):
                Crop (representing the anonymized box) to be processed.
            binary_threshold (int):
                Binary threshold to binarize image with.
            refine_padding (int):
                Padding to refine box with.
            cell (bool):
                Whether crop is a cell or not.

        Returns:
            crop_to_read (np.ndarray):
                Crop to read text from.
        """
        if refine_padding:
            crop_refined, _ = self._refine_box(
                crop=crop,
                binary_threshold=binary_threshold,
                padding=refine_padding,
                cell=cell,
            )
            if crop_refined is False:
                return []
        else:
            crop_refined = crop

        box_length = crop_refined.shape[1]
        scale = self._get_scale(box_length=box_length)
        crop_scaled = self._scale_image(image=crop_refined, scale=scale)

        # Ensure that highest pixel value is 255, else
        # sharpening might not work as expected.
        crop_scaled = np.array(crop_scaled / crop_scaled.max() * 255, dtype=np.uint8)

        crop_boundary = self._add_boundary(
            image=crop_scaled, padding=self.config.process.anonymized_box_crop_padding
        )
        if cell:
            return [crop_boundary]

        sharpened = (
            np.array(
                skimage.filters.unsharp_mask(crop_scaled, radius=20, amount=1),
                dtype=np.uint8,
            )
            * 255
        )
        sharpened_boundary = self._add_boundary(
            image=sharpened, padding=self.config.process.anonymized_box_crop_padding
        )

        crops_to_read = [crop_boundary, sharpened_boundary]

        return crops_to_read

    def _get_scale(self, box_length: int) -> float:
        """Get scale to scale box/crop with.

        Args:
            box_length (int):
                Length of box.

        Returns:
            float:
                Scale to scale box/crop with.
        """
        scale: float
        if box_length > LENGTH_SIX_LETTERS:
            scale = 1
            return scale
        scale = LENGTH_SIX_LETTERS / box_length
        scale = min(scale, self.config.process.max_scale)
        return scale

    def _scale_image(self, image: np.ndarray, scale: float) -> np.ndarray:
        """Scale image.

        Args:
            image (np.ndarray):
                Image to scale.
            scale (float):
                Scale to scale image with.

        Returns:
            np.ndarray:
                Scaled image.
        """
        if scale == 1:
            return image
        scaled = cv2.resize(image, (0, 0), fx=scale, fy=scale)
        return scaled

    def _refine_box(
        self,
        crop: np.ndarray,
        binary_threshold: int,
        box: dict = {},
        padding: int = 0,
        cell: bool = False,
    ) -> tuple:
        """Refine crop.

        Args:
            crop (np.ndarray):
                Crop of image representing the box.
            binary_threshold (int):
                Binary threshold to binarize image with.
            box (dict):
                Anonymized/cell box with coordinates.
            padding (int):
                Padding to refine box with.
            cell (bool):
                Whether crop is a cell or not.

        Returns:
            box_refined (dict):
                Refined box with coordinates.
        """
        n, m = crop.shape

        binary = self._binarize(
            image=crop,
            threshold=binary_threshold,
            val_min=0,
            val_max=255,
        )

        rows, cols = np.where(binary > 0)

        if not cell:
            # Ignore starting symbols as *'^
            mid = n // 2
            col_first = m - 1
            # col_last = 0
            for blob in self._get_blobs(binary):
                blob_row_min, blob_col_min, blob_row_max, blob_col_max = blob.bbox
                if mid in range(blob_row_min, blob_row_max):
                    col_first = min(col_first, blob_col_min)
                    # col_last = max(col_last, blob_col_max)

            if col_first == m - 1:
                return False, None
        else:
            col_first = cols.min()

        col_last = cols.max()
        row_first, row_last = rows.min(), rows.max()
        p = padding

        # Ensure that new coordinates are in [0, n) x [0, m)
        row_first_ = max(row_first - p, 0)
        col_first_ = max(col_first - p, 0)
        row_last_ = min(row_last + 1 + p, n)
        col_last_ = min(col_last + 1 + p, m)
        crop_refined = crop[row_first_:row_last_, col_first_:col_last_]
        if not box:
            return crop_refined, None

        # Padding here could make the box coordinates go out of bounds.
        box_refined = {
            "coordinates": (
                box["coordinates"][0] + row_first_,
                box["coordinates"][1] + col_first_,
                box["coordinates"][2] - (n - row_last_),
                box["coordinates"][3] - (m - col_last_),
            ),
            "origin": box["origin"],
        }

        return crop_refined, box_refined

    def _find_anonymized_boxes(self, image: np.ndarray) -> List[dict]:
        """Finds anonymized boxes in image.

        Args:
            image (np.ndarray):
                Image to find anonymized boxes in.

        Returns:
            List[dict]:
                List of anonymized boxes.
        """
        # Mean filter to make text outside boxes
        # brigther than color of boxes.
        footprint = np.ones((5, 5))
        averaged = rank.mean(image, footprint=footprint)

        binary = self._binarize(
            image=averaged,
            threshold=self.config.process.threshold_binarize_anonymized_boxes,
            val_min=0,
            val_max=255,
        )

        inverted = cv2.bitwise_not(binary)

        # Some boxes are overlapping (horizontally).
        # Split them into separate boxes.
        inverted_boxes_split = self._split_boxes_in_image(inverted=inverted.copy())

        inverted_boxes_split_2 = self._split_boxes_vertically(
            binary=inverted_boxes_split
        )

        def sort_function(blob):
            return blob.area

        blobs = self._get_blobs(
            binary=inverted_boxes_split_2, sort_function=sort_function
        )

        anonymized_boxes = []
        for blob in blobs:
            if blob.area < self.config.process.box_area_min:
                # Blob is too small to be considered an anonymized box.
                break

            if not self._conditions_for_box(blob=blob):
                continue
            height = blob.bbox[2] - blob.bbox[0]
            if height > self.config.process.box_height_upper:
                logger.info("Blob not splitted correctly with initial methods.")
                anonymized_boxes += self._split_blob_to_multiple_boxes(blob=blob)
            else:
                box_coordinates = self._blob_to_box_coordinates(blob=blob)

                anonymized_box = {
                    "coordinates": box_coordinates,
                    "origin": self.config.process.origin_box,
                }
                anonymized_boxes.append(anonymized_box)

        return anonymized_boxes

    def _remove_black_border(self, blob_image: np.ndarray) -> np.ndarray:
        """Remove black border from blob image.

        Args:
            blob_image (np.ndarray):
                Image of blob.

        Returns:
            np.ndarray:
                Image of blob with black border removed.
        """
        inverted = cv2.bitwise_not(blob_image)
        blobs = self._get_blobs(inverted)
        for blob_ in blobs:
            if self._touches_boundary(binary_crop=inverted, blob=blob_):
                coords = blob_.coords
                blob_image[coords[:, 0], coords[:, 1]] = 255
        return blob_image

    def _split_blob_to_multiple_boxes(self, blob: RegionProperties) -> List[dict]:
        """Split blob of multiple boxes.

        This function is called if a blob is not splitted
        correctly with initial methods.

        Args:
            blob (RegionProperties):
                Blob to split into multiple boxes.

        Returns:
            List[dict]:
                List of anonymized boxes.
        """
        blob_image = np.array(blob.image * 255, dtype=np.uint8)
        blob_image = self._remove_black_border(blob_image=blob_image)

        inverted = cv2.bitwise_not(blob_image)
        blobs = self._get_blobs(inverted)
        for blob_ in blobs:
            if self._touches_boundary(binary_crop=inverted, blob=blob_):
                coords = blob_.coords
                blob_image[coords[:, 0], coords[:, 1]] = 255

        booled = np.all(blob_image, axis=1)
        row_splits = []

        count = 0
        for i in range(len(booled)):
            if booled[i]:
                count += 1
            else:
                if count > self.config.process.box_split_white_space:
                    row_splits.append(
                        i - self.config.process.box_split_white_space // 2
                    )
                count = 0
        for row in row_splits:
            blob_image[row, :] = 0

        blobs = self._get_blobs(blob_image)

        boxes = []
        for blob in blobs:
            if blob.area < self.config.process.box_area_min:
                # Blob is too small to be considered an anonymized box.
                break
            if not self._conditions_for_box(blob=blob):
                continue
            box_coordinates = self._blob_to_box_coordinates(blob=blob)
            anonymized_box = {
                "coordinates": box_coordinates,
                "origin": self.config.process.origin_box,
            }
            boxes.append(anonymized_box)
        return boxes

    def _split_boxes_vertically(self, binary: np.ndarray) -> np.ndarray:
        """Split vertically overlapping boxes.

        Args:
            binary (np.ndarray):
                Binary image.

        Returns:
            np.ndarray:
                Binary image with vertically overlapping boxes split.
        """
        blobs = self._get_blobs(binary=binary)
        for blob in blobs:
            if blob.area_bbox < self.config.process.box_area_min:
                break
            blob_image = np.array(blob.image * 255, dtype=np.uint8)
            closed = cv2.morphologyEx(blob_image, cv2.MORPH_CLOSE, np.ones((20, 1)))
            opening = cv2.morphologyEx(closed, cv2.MORPH_OPEN, np.ones((15, 1)))

            booled = np.any(opening, axis=0)
            empty_cols = np.where(np.logical_not(booled))[0]
            if len(empty_cols) == 0:
                continue

            split_cols = []

            count = 1
            for i in range(1, len(empty_cols)):
                col_prev = empty_cols[i - 1]
                col = empty_cols[i]
                if col - col_prev == 1:
                    count += 1
                else:
                    if count > 7:
                        split_cols.append(empty_cols[i - 1])
                    count = 1
            if count > 7:
                split_cols.append(empty_cols[-1])

            for col in split_cols:
                row_min, col_min, row_max, _ = blob.bbox
                binary[row_min:row_max, col_min + col] = 0

        return binary

    def _blob_to_box_coordinates(self, blob: RegionProperties) -> List[int]:
        """Convert blob to box coordinates.

        Some times when boxes are splitted horizontally, a top box might
        for example containt a long horizontal line in the bottom
        that actually belongs to the bottom box. This functions removes
        such lines.

        Args:
            blob (RegionProperties):
                Blob to convert to box coordinates.

        Returns:
            List[int]:
                Box coordinates.
        """
        rows, cols = blob.coords.T
        row_center, _ = blob.centroid

        # Get col_min and col_max
        indices_upper = np.where(rows < row_center)[0]
        indices_lower = np.where(rows > row_center)[0]

        col_max_upper = cols[indices_upper].max()
        col_max_lower = cols[indices_lower].max()

        col_min_upper = cols[indices_upper].min()
        col_min_lower = cols[indices_lower].min()

        col_max = min(col_max_upper, col_max_lower) + 1
        col_min = max(col_min_upper, col_min_lower)

        # Get row_min and row_max
        row_indices_left = np.where(cols == col_min)[0]

        row_indices_right = np.where(cols == col_max - 1)[0]

        row_min_idx = max(row_indices_left.min(), row_indices_right.min())
        row_max_idx = min(row_indices_left.max(), row_indices_right.max())
        row_min = rows[row_min_idx]
        row_max = rows[row_max_idx] + 1

        box_coordinates = [
            row_min - self.config.process.shift_up,
            col_min,
            row_max,
            col_max,
        ]
        return box_coordinates

    def _conditions_for_box(self, blob: RegionProperties) -> bool:
        """Checks if conditions for box are met.

        Args:
            blob (RegionProperties):
                Blob to check conditions for.

        Returns:
            bool:
                True if conditions for box are met. False otherwise.
        """
        box_height = blob.bbox[2] - blob.bbox[0]
        box_width = blob.bbox[3] - blob.bbox[1]

        return (
            blob.area_convex / blob.area_bbox > self.config.process.box_accept_ratio
            and box_height > self.config.process.box_height_min
            and box_width > self.config.process.box_width_min
        )

    def _split_boxes_in_image(self, inverted: np.ndarray) -> np.ndarray:
        """Splits overlapping boxes in image.

        Some boxes are overlapping horizontally.
        This function splits them into separate boxes.

        Args:
            inverted (np.ndarray):
                Inverted binary image used to find the blobs/boxes.


        Returns:
            np.ndarray:
                Inverted binary image with overlapping boxes split into separate boxes.
        """
        blobs = self._get_blobs(inverted)

        # First split multiple boxes into separate boxes
        for blob in blobs:
            if blob.area_bbox < self.config.process.box_area_min:
                break
            row_min, col_min, row_max, col_max = blob.bbox

            # Blob to uint8 image
            blob_image = np.array(blob.image * 255, dtype=np.uint8)

            box_height = row_max - row_min
            if box_height > 2 * BOX_HEIGHT_LOWER_BOUND:
                # Horizontal splits

                # Get indices of rows to split
                row_indices_to_split = self._get_row_indices_to_split(
                    blob_image=blob_image
                )

                row_min, col_min, row_max, col_max = blob.bbox

                # Split
                for row_idx in row_indices_to_split:
                    row_idx_ = row_min + row_idx - self.config.process.box_split_delta
                    inverted[row_idx_, col_min : col_max + 1] = 0

        return inverted

    def _get_row_indices_to_split(self, blob_image: np.ndarray) -> List[int]:
        """Split blob of overlapping boxes into separate boxes.

        Split blob where horizontal edges are found.

        Args:
            blob_image (np.ndarray):
                uint8 image of the found blobs.

        Returns:
            List[int]:
                List of row indices to split.
        """
        closed = cv2.morphologyEx(blob_image, cv2.MORPH_CLOSE, np.ones((40, 1)))
        opening = cv2.morphologyEx(closed, cv2.MORPH_OPEN, np.ones((30, 1)))

        edges_h = self._get_horizontal_edges(closed=opening)

        edge_lengths = self._get_edge_lengths(edges_h=edges_h)

        rows_to_split = self._rows_to_split(edge_lengths=edge_lengths)
        return rows_to_split

    def _rows_to_split(self, edge_lengths: dict) -> List[int]:
        """Get rows to split blob of overlapping boxes into separate boxes.

        Args:
            edge_lengths (dict):
                Dictionary with indices and lengths of horizontal edges.

        Returns:
            List[int]:
                List of row indices to split.
        """
        if not edge_lengths:
            return []

        rows_to_split = sorted(
            edge_lengths, key=lambda k: edge_lengths[k], reverse=True
        )
        rows_to_split = [
            row
            for row in rows_to_split
            if edge_lengths[row] > self.config.process.indices_to_split_edge_min_length
        ]

        for i in range(len(rows_to_split) - 1, 0, -1):
            diffs = [abs(rows_to_split[i] - rows_to_split[j]) for j in range(i)]
            if min(diffs) < self.config.process.indices_to_split_row_diff:
                rows_to_split.pop(i)

        return rows_to_split

    def _get_edge_lengths(self, edges_h: np.ndarray):
        """Get lengths of horizontal edges.

        Args:
            edges_h (np.ndarray):
                Horizontal edges.

        Returns:
            dict:
                Dictionary with indices and lengths of horizontal edges.
        """
        edge_row_indices = np.where(edges_h > 0)[0]
        if len(edge_row_indices) == 0:
            return dict()
        indices, lengths = np.unique(edge_row_indices, return_counts=True)
        edge_lengths = dict(zip(indices, lengths))

        edges_grouped = self._group_edges(indices)
        edge_lengths_merged = self._merge_adjacent_edges(
            edges_grouped=edges_grouped, edge_lengths=edge_lengths
        )

        return edge_lengths_merged

    @staticmethod
    def _group_edges(indices: np.ndarray):
        """Group indices of horizontal edges.

        Adjacent indices are grouped together.

        Args:
            indices (np.ndarray):
                Indices of horizontal edges.

        Returns:
            List[List[int]]:
                List of grouped indices.
        """
        edges_grouped = [[indices[0]]]

        adjacent_indices = np.diff(indices) == 1
        for i in range(1, len(indices)):
            if adjacent_indices[i - 1]:
                edges_grouped[-1].append(indices[i])
            else:
                edges_grouped.append([indices[i]])
        return edges_grouped

    def _merge_adjacent_edges(self, edges_grouped: List[List[int]], edge_lengths: dict):
        """Merge adjacent edges.

        Adjacent edges are merged together. The edge in each group with
        the largest length is used as the index for the merged edge.

        Args:
            edges_grouped (List[List[int]]):
                List of grouped indices.
            edge_lengths (dict):
                Dictionary with indices and lengths of horizontal edges.

        Returns:
            dict:
                Dictionary with indices and lengths of horizontal edges.
        """
        edge_lengths_merged = dict()
        for group in edges_grouped:
            idx = self._largest_edge_in_group(group=group, edge_lengths=edge_lengths)
            total_length = sum(edge_lengths[i] for i in group)
            edge_lengths_merged[idx] = total_length
        return edge_lengths_merged

    @staticmethod
    def _largest_edge_in_group(group: List[int], edge_lengths: dict):
        """Get index of largest edge in group.

        Args:
            group (List[int]):
                List of indices.
            edge_lengths (dict):
                Dictionary with indices and lengths of horizontal edges.

        Returns:
            int:
                Index of largest edge in group.
        """
        idx = group[0]
        for i in group[1:]:
            if edge_lengths[i] > edge_lengths[idx]:
                idx = i
        return idx

    def _get_horizontal_edges(self, closed: np.ndarray) -> np.ndarray:
        """Get horizontal edges from image.

        Args:
            closed (np.ndarray):
                Image to get horizontal edges from.

        Returns:
            np.ndarray:
                All horizontal edges.
        """
        edges_h = skimage.filters.sobel_h(closed)
        edges_h = np.abs(edges_h)
        edges_h = np.array(edges_h * 255, dtype=np.uint8)
        return edges_h

    @staticmethod
    def _binarize(
        image: np.ndarray, threshold: int, val_min: int = 0, val_max: int = 1
    ) -> np.ndarray:
        """Binarize image.

        Args:
            image (np.ndarray):
                Image to be binarized.
            threshold (int):
                Threshold used to binarize the image.
            val_min (int):
                Value to be assigned to pixels below threshold.
            val_max (int):
                Value to be assigned to pixels above threshold.

        Returns:
            np.ndarray:
                Binarized image.
        """
        t = threshold
        binary = image.copy()
        binary[binary < t] = val_min
        binary[binary >= t] = val_max
        return binary

    def _remove_boundary_noise(
        self, crop: np.ndarray, binary_threshold: int
    ) -> np.ndarray:
        """Removes noise on the boundary of an anonymized box.

        All white pixels in a perfect bounding box
        should be a pixel of a relevant character.
        Some images have white pixel defect at the
        boundary of the bounding box, and
        this function removes those white pixels.

        Args:
            crop (np.ndarray):
                Image of anonymized box.
            binary_threshold (int):
                Binary threshold to binarize image with.

        Returns:
            np.ndarray:
                Cropped image (anonymized box) with boundary noise removed.
        """
        binary_crop = self._binarize(
            image=crop,
            threshold=binary_threshold,
            val_min=0,
            val_max=255,
        )
        blobs = self._get_blobs(binary_crop)

        for blob in blobs:
            row_min, col_min, row_max, col_max = blob.bbox
            height = row_max - row_min
            length = col_max - col_min

            touches_boundary = self._touches_boundary(
                binary_crop=binary_crop, blob=blob
            )
            if self._too_few_pixels(blob=blob, touches_boundary=touches_boundary) or (
                self._height_length_condition(height=height, length=length)
                and touches_boundary
                and self._low_longest_distance_from_boundary(
                    crop=binary_crop, blob=blob
                )
                and not self._closely_square(height=height, length=length)
            ):
                # Remove blob
                coords = blob.coords
                crop[coords[:, 0], coords[:, 1]] = 0
        return crop

    def _too_few_pixels(self, blob: RegionProperties, touches_boundary: bool) -> bool:
        """Checks if blob has too few pixels to be a relevant character.

        Used in _remove_boundary_noise to determine if a blob is noise or not.

        Args:
            blob (skimage.measure._regionprops._RegionProperties):
                A blob in the image.
            touches_boundary (bool):
                Whether blob touches the boundary of the image or not.

        Returns:
            bool:
                True if blob has too few pixels to
                be a relevant character. False otherwise.
        """
        coords = blob.coords
        return (
            len(coords) < self.config.process.threshold_remove_boundary_too_few_pixels
            and touches_boundary
        )

    def _low_longest_distance_from_boundary(
        self, crop: np.ndarray, blob: RegionProperties
    ) -> bool:
        """Checks if blob has a low longest distance from the boundary of the image.

        Used in _remove_boundary_noise to determine if a blob is noise or not.

        Args:
            crop (np.ndarray):
                Anonymized box.
            blob (skimage.measure._regionprops._RegionProperties):
                A blob in the image.

        Returns:
            bool:
                True if blob has a low longest distance from the
                boundary of the image. False otherwise.
        """
        n = min(crop.shape)
        return self._maximum_distance_from_boundary(crop=crop, blob=blob) < n * 0.3

    def _maximum_distance_from_boundary(
        self, crop: np.ndarray, blob: RegionProperties
    ) -> float:
        """Get maximum distance from blob to boundary of image.

        E.g. if the minimum distance from the blob to
        the top boundary of the image is 5,
        and the minimum distance from the blob to
        the bottom boundary of the image is 10,
        to the left boundary is 3, and to the right
        boundary is 7, then the maximum distance
        from the blob to the boundary of the image is 10.

        Used in _remove_boundary_noise to determine if a blob is noise or not.

        Args:
            crop (np.ndarray):
                Anonymized box.
            blob (skimage.measure._regionprops._RegionProperties):
                A blob in the image.

        Returns:
            float:
                Maximum distance from blob to boundary of image.
        """
        n, m = crop.shape
        row_boundaries = [0, n - 1]
        col_boundaries = [0, m - 1]
        rows, cols = blob.coords.transpose()

        rows_distance_to_boundary = self._min_distance_to_boundary(
            indices=rows, boundaries=row_boundaries
        )
        cols_distance_to_boundary = self._min_distance_to_boundary(
            indices=cols, boundaries=col_boundaries
        )
        # Concatenate
        concatenated = np.concatenate(
            [rows_distance_to_boundary, cols_distance_to_boundary], axis=1
        )
        min_distance_to_boundary_for_each_point = (
            self._min_distance_to_boundary_for_each_point(concatenated)
        )
        maximum_distance = np.max(min_distance_to_boundary_for_each_point)
        return maximum_distance

    @staticmethod
    def _min_distance_to_boundary(indices: np.ndarray, boundaries: List[int]):
        """Get minimum distance from indices to boundaries.

        For each index in indices, the minimum distance to a boundary is calculated.

        Args:
            indices (np.ndarray):
                Indices to calculate distance from.
            boundaries (List[int]):
                Boundaries to calculate distance to.

        Returns:
            np.ndarray:
                Minimum distance from indices to a boundary.
        """
        return np.min(np.abs(indices[:, None] - boundaries), axis=1)[:, None]

    @staticmethod
    def _min_distance_to_boundary_for_each_point(
        concatenated: np.ndarray,
    ) -> np.ndarray:
        """Get minimum distance from indices to boundaries.

        Each row in concatenated is a 2D point, where the first value
        is the shortest distance to a row boundary, and the second value
        is the shortest distance to a column boundary.
        This function returns the minimum distance from each point to a boundary.
        """
        return np.min(concatenated, axis=1)

    def _height_length_condition(self, height: int, length: int) -> bool:
        """Check if height and length of blob meets condition.

        Args:
            height (int):
                Height of blob.
            length (int):
                Length of blob.

        Returns:
            bool:
                True if height and length of blob meets condition. False otherwise.
        """
        return (
            height < self.config.process.threshold_remove_boundary_height
            or length > self.config.process.threshold_remove_boundary_length
        )

    def _closely_square(self, height: int, length: int) -> bool:
        """Check if blob is closely square.

        'Closely square' if the height and length of the blob are almost equal.

        Args:
            height (int):
                Height of blob.
            length (int):
                Length of blob.

        Returns:
            bool:
                True if blob is closely square. False otherwise.
        """
        return (
            abs(height - length)
            < self.config.process.threshold_remove_boundary_closely_square
        )

    @staticmethod
    def _touches_boundary(binary_crop: np.ndarray, blob: RegionProperties) -> bool:
        """Check if blob touches the boundary of the image.

        Used in _remove_boundary_noise to determine if a blob is noise or not.

        Args:
            binary_crop (np.ndarray):
                Anonymized box.
                (used to get the non-zero boundaries of the image).
            blob (skimage.measure._regionprops._RegionProperties):
                A blob in the image.

        Returns:
            bool:
                True if blob touches the boundary of the image. False otherwise.
        """
        for boundary in [0, *binary_crop.shape]:
            if boundary in blob.bbox:
                return True
        return False

    def _split_box(self, crop: np.ndarray, anonymized_box: dict) -> List[dict]:
        """Split box into multiple boxes - one for each word.

        Args:
            crop (np.ndarray):
                Image of the box.
            anonymized_box (dict):
                Anonymized box with coordinates.

        Returns:
            List[dict]:
                List of anonymized boxes - one for each word of the input box.
        """
        split_indices = self._get_split_indices(crop=crop)
        origin = anonymized_box["origin"]
        if not split_indices:
            return [anonymized_box]
        else:
            anonymized_boxes = []

            row_min, col_min, row_max, col_max = anonymized_box["coordinates"]
            first_box = {
                "coordinates": [row_min, col_min, row_max, col_min + split_indices[0]],
                "crop_refined_coordinates": [0, 0, row_max, split_indices[0]],
                "origin": origin,
            }

            anonymized_boxes.append(first_box)

            # Get box in between first and last box
            if len(split_indices) > 1:
                for split_index_1, split_index_2 in zip(
                    split_indices[:-1], split_indices[1:]
                ):
                    anonymized_box_ = {
                        "coordinates": [
                            row_min,
                            col_min + split_index_1 + 1,
                            row_max,
                            col_min + split_index_2,
                        ],
                        "crop_refined_coordinates": [
                            0,
                            split_index_1 + 1,
                            row_max,
                            split_index_2,
                        ],
                        "origin": origin,
                    }
                    anonymized_boxes.append(anonymized_box_)

            # Get last box
            last_box = {
                "coordinates": [
                    row_min,
                    col_min + split_indices[-1] + 1,
                    row_max,
                    col_max,
                ],
                "crop_refined_coordinates": [
                    0,
                    split_indices[-1] + 1,
                    row_max,
                    col_max,
                ],
                "origin": origin,
            }
            anonymized_boxes.append(last_box)
        return anonymized_boxes

    def _get_split_indices(self, crop: np.ndarray) -> List[int]:
        """Split box into multiple boxes - one for each word.

        Used in the function `_split_box`.

        Arg:
            crop (np.ndarray):
                Image of the box.

        Returns:
            List[int]:
                List of indices where the box should be split.
        """
        inverted = cv2.bitwise_not(crop)

        binary = self._binarize(
            inverted,
            threshold=255 - self.config.process.threshold_binarize_process_crop,
        )

        # One bool value for each column.
        # True if all pixels in column are white.
        booled = binary.all(axis=0)
        start_idx = np.where(booled == 0)[0][0]

        cumsum_reset_0 = self._cumsum_reset_0(booled[start_idx:])
        gap_indices = np.where(cumsum_reset_0 > self.config.process.threshold_gap)[0]
        if not gap_indices.size:
            return []

        gap_indices_ = [gap_indices[0]]
        for i in range(1, len(gap_indices)):
            if gap_indices[i] - gap_indices[i - 1] > 1:
                gap_indices_.append(gap_indices[i])

        gap_half = self.config.process.threshold_gap // 2
        split_indices = [start_idx + x - gap_half for x in gap_indices_]
        return split_indices

    @staticmethod
    def _cumsum_reset_0(a):
        mask = a == 0
        cumsum = a.cumsum()
        result = cumsum - np.maximum.accumulate(np.where(mask, cumsum, 0))
        return result

    @staticmethod
    def _add_boundary(image: np.ndarray, padding: int = 1) -> np.ndarray:
        """Add boundary to image.

        EasyOCR seems to give the best results when the text is
        surrounded by black pixels.

        Args:
            image (np.ndarray):
                Image to add boundary to.
            padding (int):
                Padding to add to boundary.

        Returns:
            np.ndarray:
                Image with boundary.
        """
        p = padding
        padded = np.zeros(
            (image.shape[0] + p * 2, image.shape[1] + p * 2), dtype=np.uint8
        )
        padded[p:-p, p:-p] = image
        return padded

    @staticmethod
    def _read_text_with_tika(pdf_path: str) -> str:
        """Read text from pdf with tika.

        Args:
            pdf_path (str):
                Path to pdf.

        Returns:
            str:
                Text from pdf.
        """
        request_options = {"timeout": 300}
        text = ""
        try:
            result = parser.from_file(pdf_path, requestOptions=request_options)
            if result["status"] == 200:
                text = result["content"]
        except Exception as e:
            logger.error(f"Error reading text with tika: {e}")
        return text.strip()

    @staticmethod
    def _get_text_from_pages(pages: dict) -> str:
        """Get text from pages.

        Args:
            pages (dict):
                Pages with text and extraction method.

        Returns:
            pdf_text (str):
                Text from pages.
        """
        pdf_text = "\n\n".join(page["text"] for page in pages.values())
        return pdf_text


def save_cv2_image_tmp(image):
    """Saves image to tmp.png.

    Used for debugging.
    """
    image = image.copy()
    if image.max() < 2:
        image = image * 255
    cv2.imwrite("tmp.png", image)


def draw_box(image, box, pixel_value=0):
    """Draws box on image.

    Used for debugging.
    """
    image = image.copy()
    if isinstance(box, dict):
        row_min, col_min, row_max, col_max = box["coordinates"]
        image[row_min:row_max, col_min:col_max] = pixel_value
    elif isinstance(box, ExtractedTable):
        row_min, col_min, row_max, col_max = (
            box.bbox.y1,
            box.bbox.x1,
            box.bbox.y2,
            box.bbox.x2,
        )
        image[row_min:row_max, col_min:col_max] = pixel_value
    else:
        # blob
        coords = box.coords
        image[coords[:, 0], coords[:, 1]] = pixel_value

    save_cv2_image_tmp(image)
