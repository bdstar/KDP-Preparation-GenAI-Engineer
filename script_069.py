# e.g. "How many words are in this sentence, and what is that count times 3?"
# The agent should call word_count, observe the result, call calculator on
# (count * 3), observe that, and then answer — two tool calls and a synthesis.
answer = run_agent(
    "How many words are in 'the quick brown fox jumps', and what is that number squared?",
    call_model)
print(answer)
