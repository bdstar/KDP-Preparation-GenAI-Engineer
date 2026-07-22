safe_system = SafetyLayer(
    core=pipeline,
    input_guardrails=[injection_filter, policy_check],      # Ch 30
    output_validation=ResponseSchema,                        # Pydantic, Ch 30
    output_guardrails=[content_safety_check],
)
