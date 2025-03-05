# import os
# from datetime import datetime
# from fastapi import FastAPI, File, UploadFile, HTTPException
# from google.cloud import speech_v1p1beta1 as speech
# import boto3


# # AWS S3 Configuration
# AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
# AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
# S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

# s3_client = boto3.client(
#     "s3",
#     aws_access_key_id=AWS_ACCESS_KEY,
#     aws_secret_access_key=AWS_SECRET_KEY,
# )

# # Google Speech-to-Text Client
# client = speech.SpeechClient()

# # Upload file to S3
# def upload_to_s3(file: UploadFile) -> str:
#     try:
#         file_name = f"audio_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp3"
#         s3_client.upload_fileobj(file.file, S3_BUCKET_NAME, file_name)
#         return f"https://{S3_BUCKET_NAME}.s3.amazonaws.com/{file_name}"
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))