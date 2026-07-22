def budget_report(components: dict, count, limit: int):
    used = {name: count(text) for name, text in components.items()}
    total = sum(used.values())
    for name, n in used.items():
        print(f"  {name:16s} {n:6d} tokens ({n/total:.0%})")
    print(f"  {'TOTAL':16s} {total:6d} / {limit} tokens "
          f"({'OK' if total <= limit else 'OVER BUDGET'})")
    return total
