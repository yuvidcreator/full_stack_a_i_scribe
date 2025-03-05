from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.sql import func
from database.db import Base

class Transcription(Base):
    __tablename__ = "transcriptions"

    id = Column(Integer, primary_key=True, index=True)
    input_text = Column(Text, nullable=True)
    output_text = Column(Text, nullable=False)
    language = Column(String(10), nullable=False)
    created_at = Column(TIMESTAMP, default=func.now())