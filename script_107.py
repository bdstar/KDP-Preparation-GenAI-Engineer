import time, logging
log = logging.getLogger("agent-obs")
 
def observed_run(user_input: str, run_agent, count_tokens):
    start = time.time()
    trace = {"input": user_input, "steps": []}          # full trace of the request
    allowed, reason = input_guardrail(user_input)
    if not allowed:
        log.warning(f"blocked input: {reason}")
        return AgentResponse(answer="I can't process that.", confidence=1.0)
    raw = run_agent(user_input, trace=trace)            # agent records steps into trace
    response = validate_response(raw) or AgentResponse(answer="Sorry, please retry.",
                                                       confidence=0.0)
    response = output_guardrail(response)
    log.info(f"latency_ms={(time.time()-start)*1000:.0f} "
             f"tokens={count_tokens(raw)} steps={len(trace['steps'])}")  # metrics + cost
    return response
