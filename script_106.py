def output_guardrail(response: AgentResponse) -> AgentResponse:
    """Check content safety/policy on well-formed output before returning it."""
    if contains_unsafe_content(response.answer):        # policy check / safety rail
        return AgentResponse(answer="I can't help with that request.",
                             confidence=1.0, sources=[])
    return response
