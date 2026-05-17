import base64
import io
from pdf2image import convert_from_path


class PDFReaderImg:
    def __init__(self, path: str, dpi: int = 150):
        self.path = path
        self.dpi = dpi
        self._pages = convert_from_path(path, dpi=dpi)

    @property
    def page_count(self) -> int:
        return len(self._pages)

    def _to_base64(self, index: int) -> str:
        buf = io.BytesIO()
        self._pages[index].save(buf, format="PNG")
        return base64.b64encode(buf.getvalue()).decode()

    def page_as_block(self, index: int) -> dict:
        """Returns a single page as a Claude image content block."""
        return {
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": "image/png",
                "data": self._to_base64(index),
            },
        }

    def all_as_blocks(self) -> list[dict]:
        """Returns all pages as a list of Claude image content blocks."""
        return [self.page_as_block(i) for i in range(self.page_count)]

    def range_as_blocks(self, start: int, end: int) -> list[dict]:
        """Returns pages start to end (0-indexed, end exclusive) as content blocks."""
        return [self.page_as_block(i) for i in range(start, min(end, self.page_count))]
