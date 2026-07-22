def transcribe(audio_path: str) -> str:
    from faster_whisper import WhisperModel          # an optimized Whisper (Section 22.4)
    model = WhisperModel("base")                      # size trades accuracy vs speed
    segments, _ = model.transcribe(audio_path)
    return " ".join(seg.text for seg in segments)     # the user's spoken question, as text
