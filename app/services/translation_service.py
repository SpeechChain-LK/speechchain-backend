# app/services/translation_service.py
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

# Load tokenizer and model (once)
tokenizer = MBart50TokenizerFast.from_pretrained("app/models/mbart50")
model = MBartForConditionalGeneration.from_pretrained("app/models/mbart50")

# Set source language (Tamil)
tokenizer.src_lang = "ta_IN"

def translate(tamil_text):
    # Tokenize Tamil input
    inputs = tokenizer(tamil_text, return_tensors="pt")

    # Generate Sinhala translation
    generated_tokens = model.generate(**inputs, forced_bos_token_id=tokenizer.lang_code_to_id["si_LK"])

    sinhala_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]

    return sinhala_text
