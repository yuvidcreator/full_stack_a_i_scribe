import boto3
from settings.base import settings

s3_client = boto3.client(
    "s3",
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
)

def upload_to_s3(file_path: str, file_name: str):
    s3_client.upload_file(file_path, settings.S3_BUCKET, file_name)