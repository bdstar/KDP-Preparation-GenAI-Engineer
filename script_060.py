def ingest_folder(folder: str) -> tuple[list[dict], list[str]]:
    all_chunks, failures = [], []
    for path in Path(folder).glob("*.pdf"):
        try:
            all_chunks.extend(ingest(str(path)))
        except Exception as e:
            failures.append(f"{path.name}: {e}")     # log and continue
    return all_chunks, failures
