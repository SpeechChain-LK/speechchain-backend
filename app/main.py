# app/main.py
from fastapi import FastAPI, UploadFile, File
from app.services import asr_service

app = FastAPI(title="SpeechChain LK")

@app.post("/asr/")
async def asr_endpoint(file: UploadFile = File(...)):
    audio_bytes = await file.read()
    tamil_text = asr_service.transcribe(audio_bytes)
    return {"transcription": tamil_text}
