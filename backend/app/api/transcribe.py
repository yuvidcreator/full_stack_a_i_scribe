# API Endpoint: Upload and Transcribe Audio
import openai
from fastapi import File, UploadFile, Form, Depends
from fastapi.responses import JSONResponse

from main import app
from database import crud
from app.services.cloud_service import upload_to_s3
from app.services.ai_service import transcribe_audio


@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    # Upload file to S3
    s3_url = upload_to_s3(file)
    
    # Transcribe audio
    transcription = transcribe_audio(file)
    
    return {
        "s3_url": s3_url,
        "transcription": transcription,
    }



@app.post("/process-text")
async def process_text(text: str = Form(...), language: str = Form(...), db: Session = Depends(get_db)):
    # Simulate AI processing (replace with actual AI logic)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        max_tokens=100,
    )
    output_text = response.choices[0].text.strip()

    # Save to database
    crud.create_transcription(db, input_text=text, output_text=output_text, language=language)

    return JSONResponse(content={"output": output_text})



@app.post("/process-voice")
async def process_voice(file: UploadFile = File(...), language: str = Form(...), db: Session = Depends(get_db)):
    # Save file locally
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    # Upload to S3
    upload_to_s3(file_path, file.filename)

    # Transcribe audio
    output_text = transcribe_audio(file_path, language=language)

    # Save to database
    crud.create_transcription(db, input_text=None, output_text=output_text, language=language)

    # Clean up
    os.remove(file_path)

    return JSONResponse(content={"output": output_text})