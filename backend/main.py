import os
from fastapi import FastAPI, File, UploadFile, Form, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

import openai
from app import api_router
from database import SessionLocal, engine
from app.services.ai_service import transcribe_audio
from fastapi.middleware.cors import CORSMiddleware


from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    api_router,
    prefix='/api'
)

