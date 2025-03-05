# import os
import openai
from settings.base import settings

openai.api_key = settings.OPENAI_API_KEY

def transcribe_audio(file_path: str, language: str = "en"):
    with open(file_path, "rb") as audio_file:
        transcription = openai.Audio.transcribe("whisper-1", audio_file, language=language)
    return transcription["text"]