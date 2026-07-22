def parse_naive(path: str) -> str:
    """Fast, crude extraction — pulls whatever text stream the PDF exposes."""
    from pypdf import PdfReader
    reader = PdfReader(path)
    return "\n".join((page.extract_text() or "") for page in reader.pages)
