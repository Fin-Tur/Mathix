import pypdf


class PDFReader:
    def __init__(self, path: str):
        self.path = path
        self._reader = pypdf.PdfReader(path)

    @property
    def page_count(self) -> int:
        return len(self._reader.pages)

    def read_page(self, index: int) -> str:
        """Returns the text of a single page (0-indexed)."""
        return self._reader.pages[index].extract_text() or ""

    def read_all(self) -> str:
        """Returns the full text of the entire PDF."""
        pages = []
        for i, page in enumerate(self._reader.pages):
            text = page.extract_text()
            if text:
                pages.append(f"[Page {i + 1}]\n{text.strip()}")
        return "\n\n".join(pages)

    def read_range(self, start: int, end: int) -> str:
        """Returns text from page start to end (0-indexed, end exclusive)."""
        pages = []
        for i in range(start, min(end, self.page_count)):
            text = self._reader.pages[i].extract_text()
            if text:
                pages.append(f"[Page {i + 1}]\n{text.strip()}")
        return "\n\n".join(pages)
