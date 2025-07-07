# app/main.py
from fastapi import FastAPI, UploadFile, File
from app.services import asr_service, translation_service

app = FastAPI(title="SpeechChain LK API")

@app.post("/speechchain/")
async def asr_and_translate(file: UploadFile = File(...)):
    audio_bytes = await file.read()
    
    # 1️⃣ Transcribe Tamil
    tamil_text = asr_service.transcribe(audio_bytes)
    
    # 2️⃣ Translate to Sinhala
    sinhala_text = translation_service.translate(tamil_text)

    return {
        "tamil_transcription": tamil_text,
        "sinhala_translation": sinhala_text
    }