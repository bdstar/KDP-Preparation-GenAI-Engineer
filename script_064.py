THRESHOLDS = {"faithfulness": 0.85, "answer_relevancy": 0.80,
              "context_recall": 0.75, "context_precision": 0.70}
 
def quality_gate(report) -> bool:
    passed = all(report[m] >= t for m, t in THRESHOLDS.items())
    for m, t in THRESHOLDS.items():
        flag = "ok" if report[m] >= t else "FAIL"
        print(f"  {m:18s} {report[m]:.2f} (min {t}) [{flag}]")
    return passed          # in CI: exit non-zero when this is False
