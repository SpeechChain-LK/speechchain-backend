# app/services/asr_service.py
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import librosa
import torch
import tempfile

# Load model and processor once when the service starts
processor = WhisperProcessor.from_pretrained("app/models/whisper")
model = WhisperForConditionalGeneration.from_pretrained("app/models/whisper")

def transcribe(audio_bytes):
    # Save audio temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(audio_bytes)
        temp_audio_path = temp_audio.name

    # Load audio using librosa
    audio, sr = librosa.load(temp_audio_path, sr=16000)

    # Preprocess
    input_features = processor(audio, sampling_rate=16000, return_tensors="pt").input_features
    forced_decoder_ids = processor.get_decoder_prompt_ids(language="ta", task="transcribe")

    # Inference
    predicted_ids = model.generate(input_features, forced_decoder_ids=forced_decoder_ids)
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]

    return transcription
