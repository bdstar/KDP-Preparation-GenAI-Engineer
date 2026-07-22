def run_agent(goal: str, call_model, max_steps: int = 6) -> str:
    messages = [{"role": "system", "content":
                 "Reason step by step. To use a tool, respond with JSON "
                 '{"tool": name, "args": {...}}. To finish, respond with '
                 '{"answer": "..."}. Tools: ' + str(TOOL_SCHEMAS)},
                {"role": "user", "content": goal}]
    for _ in range(max_steps):                       # iteration limit = guardrail
        reply = call_model(messages)                 # the model's next decision
        step = parse_json(reply)
        if "answer" in step:                         # model chose to finish
            return step["answer"]
        tool, args = step["tool"], step.get("args", {})
        try:
            observation = TOOLS[tool](**args)        # execute the action
        except Exception as e:
            observation = f"ERROR: {e}"              # structured error feedback
        messages.append({"role": "assistant", "content": reply})
        messages.append({"role": "user", "content": f"Observation: {observation}"})
    return "Stopped: reached the step limit without finishing."
