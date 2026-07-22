def input_guardrail(user_input: str) -> tuple[bool, str]:
    """Return (allowed, reason). Block obvious injection / misuse before the model."""
    lowered = user_input.lower()
    injection_signals = ["ignore previous instructions", "disregard your rules",
                         "reveal your system prompt"]
    if any(sig in lowered for sig in injection_signals):
        return False, "possible prompt injection"
    # A real guardrail also uses a classifier / a guardrail framework for nuance,
    # since a fixed list misses paraphrased and novel attempts.
    return True, "ok"
