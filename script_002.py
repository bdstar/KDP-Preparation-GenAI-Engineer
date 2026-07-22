def collect_scores(stack: list[Competency]) -> None:
    for c in stack:
        raw = input(f"{c.name} — current level 0-5 (target {c.target}): ")
        c.current = int(raw) if raw.strip().isdigit() else 0
 
def save(stack: list[Competency], path: Path) -> None:
    data = [{"name": c.name, "target": c.target, "current": c.current} for c in stack]
    path.write_text(json.dumps(data, indent=2))
