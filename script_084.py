def speak(text: str, out_path: str = "reply.mp3"):
    tts_client.synthesize(text=text, voice="support-agent", output=out_path)  # e.g. ElevenLabs
    play(out_path)                                    # play the spoken reply to the user
