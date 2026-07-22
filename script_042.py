GOLDEN = [
    {"review": "An absolute masterpiece from start to finish.", "expected": "positive"},
    {"review": "I want my two hours back.",                     "expected": "negative"},
    {"review": "It was fine, nothing special.",                 "expected": "neutral"},
]
 
def evaluate(prompt: PromptVersion, call_model) -> float:
    correct = 0
    for case in GOLDEN:
        out = call_model(prompt.render(review=case["review"])).strip().lower()
        correct += case["expected"] in out
    return correct / len(GOLDEN)   # accuracy on the golden set
call_modelcount_tokens
def ab_test(variant_a, variant_b, call_model, count_tokens):
    for label, p in [("A", variant_a), ("B", variant_b)]:
        acc = evaluate(p, call_model)
        avg_tokens = sum(count_tokens(p.render(review=c["review"])) for c in GOLDEN) / len(GOLDEN)
        print(f"[{label}] v{p.version}: accuracy={acc:.0%}, avg_prompt_tokens={avg_tokens:.0f}")
 
# ab_test(classify_v1, classify_v2, call_model, count_tokens)
