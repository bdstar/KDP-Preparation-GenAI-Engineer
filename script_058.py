def parse_structured(path: str) -> str:
    """Layout- and table-aware parsing into clean Markdown."""
    from docling.document_converter import DocumentConverter
    result = DocumentConverter().convert(path)
    return result.document.export_to_markdown()   # tables preserved as Markdown
