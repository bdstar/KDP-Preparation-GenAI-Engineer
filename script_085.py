def voice_turn(audio_path: str):
    question = transcribe(audio_path)                 # speech -> text
    reply = answer(question)                          # text -> agent reasoning -> text
    speak(reply)                                      # text -> speech
    print(f"User: {question}\nAgent: {reply}")
# In a real agent, a framework (Section 22.7) manages the real-time audio flow,
# interruptions, and turn-taking around this loop.
