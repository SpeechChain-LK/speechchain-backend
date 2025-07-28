# app/services/sinhala_translation_service.py
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

# Load tokenizer and model for Sinhala to Tamil translation
tokenizer = MBart50TokenizerFast.from_pretrained("app/models/Sinhala-To-Tamil/mbart50")
model = MBartForConditionalGeneration.from_pretrained("app/models/Sinhala-To-Tamil/mbart50")

# Set source language (Sinhala)
tokenizer.src_lang = "si_LK"

def translate(sinhala_text):
    # Tokenize Sinhala input
    inputs = tokenizer(sinhala_text, return_tensors="pt")

    # Generate Tamil translation
    generated_tokens = model.generate(**inputs, forced_bos_token_id=tokenizer.lang_code_to_id["ta_IN"])

    tamil_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]

    return tamil_text
