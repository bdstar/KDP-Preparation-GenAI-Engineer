def prioritized_plan(stack: list[Competency]) -> list[Competency]:
    # sort by largest gap first; ties keep original (bottom-up) order
    return sorted(stack, key=lambda c: c.gap, reverse=True)
 
def print_plan(stack: list[Competency]) -> None:
    plan = prioritized_plan(stack)
    print("\n=== Prioritized learning & portfolio plan ===")
    for i, c in enumerate(plan, 1):
        if c.gap == 0:
            continue
        print(f"{i}. {c.name}: level {c.current} -> {c.target} (gap {c.gap})")
