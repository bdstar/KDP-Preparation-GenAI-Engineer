def answer(question: str) -> str:
    # A support agent with tools (order lookup, KB search) from earlier chapters.
    result = support_agent.run(question)              # reason + call tools + respond
    return result.text                                # the agent's textual answer
