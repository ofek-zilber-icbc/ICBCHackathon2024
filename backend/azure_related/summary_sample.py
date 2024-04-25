import assemblyai as aai

aai.settings.api_key = "1646ca3a00194e2a8a8421214fe1d387"

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(
    "call2.wav",
    config = aai.TranscriptionConfig(summarization=True)
)

print(transcript.summary)