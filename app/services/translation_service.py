# # app/services/translation_service.py
# from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

# # Load mBART50 model (load only once)
# tokenizer = MBart50TokenizerFast.from_pretrained("app/models/mbart50")
# model = MBartForConditionalGeneration.from_pretrained("app/models/mbart50")

# tokenizer.src_lang = "ta_IN"

# def translate(tamil_text):
#     inputs = tokenizer(tamil_text, return_tensors="pt")
#     generated_tokens = model.generate(**inputs, forced_bos_token_id=tokenizer.lang_code_to_id["si_LK"])
#     sinhala_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
#     return sinhala_text
