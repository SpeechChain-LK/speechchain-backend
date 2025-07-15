# app/main.py
from fastapi import FastAPI, UploadFile, File, HTTPException
from app.services import asr_service, translation_service
import traceback

app = FastAPI(title="SpeechChain LK API")

@app.post("/speechchain/")
async def asr_and_translate(file: UploadFile = File(...)):
    try:
        print(f"Received file: {file.filename}")
        print(f"Content type: {file.content_type}")
        print(f"File size: {file.size}")
        
        audio_bytes = await file.read()
        print(f"Audio bytes length: {len(audio_bytes)}")
        
        if len(audio_bytes) == 0:
            raise HTTPException(status_code=400, detail="Empty audio file")
        
        # 1️⃣ Transcribe Tamil
        tamil_text = asr_service.transcribe(audio_bytes)
        
        # 2️⃣ Translate to Sinhala
        sinhala_text = translation_service.translate(tamil_text)

        return {
            "tamil_transcription": tamil_text,
            "sinhala_translation": sinhala_text
        }
    except Exception as e:
        print(f"Error processing request: {str(e)}")
        print(f"Traceback: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")

@app.get("/ping/")
async def pingpong():
    return {
        "result" : "pong"
    }