# from fastapi import FastAPI, File, UploadFile, HTTPException
# from google.cloud import speech_v1p1beta1 as speech
# from app.services.cloud import client

# # Transcribe audio using Google Speech-to-Text
# def transcribe_audio(file: UploadFile) -> str:
#     try:
#         content = file.file.read()
#         audio = speech.RecognitionAudio(content=content)
#         config = speech.RecognitionConfig(
#             encoding=speech.RecognitionConfig.AudioEncoding.MP3,
#             sample_rate_hertz=16000,
#             language_code="en-US",
#         )
#         response = client.recognize(config=config, audio=audio)
#         transcription = ""
#         for result in response.results:
#             transcription += result.alternatives[0].transcript
#         return transcription
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))