from sqlalchemy.orm import Session
from database import models

def create_transcription(db: Session, input_text: str, output_text: str, language: str):
    db_transcription = models.Transcription(
        input_text=input_text,
        output_text=output_text,
        language=language,
    )
    db.add(db_transcription)
    db.commit()
    db.refresh(db_transcription)
    return db_transcription