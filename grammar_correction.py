from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

model_name = "vennify/t5-base-grammar-correction"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
grammar_corrector = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

def correct_text(text):
    corrected_output = grammar_corrector(text, max_length=256, do_sample=False)[0]['generated_text']
    return corrected_output
