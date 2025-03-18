import gradio as gr # i used this for to create the web app
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline  # Transformers Library gives us access to many pre-trained models like T5

# Initialize the T5-based grammar correction model
model_name = "vennify/t5-base-grammar-correction"
tokenizer = AutoTokenizer.from_pretrained(model_name) # Loads the tokenizer that will convert the input text into a format that the model can understand
model = AutoModelForSeq2SeqLM.from_pretrained(model_name) # Loads the actual AI model that will generate the corrected senetnces
grammar_corrector = pipeline("text2text-generation", model=model, tokenizer=tokenizer) #A helper that makes it easier to use the model.

def autocorrect_text(input_text):
    corrected_output = grammar_corrector(input_text, max_length=256, do_sample=False)[0]['generated_text']
    return corrected_output

with gr.Blocks() as demo:
    gr.Markdown("# Autocorrector-AI/ Powered By Kushan Sankalpa")
    gr.Markdown("Type or paste your text below and see the corrected version.")
    
    text_input = gr.Textbox(label="Input Text", lines=6, placeholder="Enter text here...")
    text_output = gr.Textbox(label="Corrected Text", lines=6)
    
    def correct_button_action(input_text):
        return autocorrect_text(input_text)

    correct_button = gr.Button("Correct Text")
    correct_button.click(fn=correct_button_action, inputs=text_input, outputs=text_output)
    
    # Add a Clear button to reset the input and output fields
    clear_button = gr.Button("Clear")
    def clear_action():
        return "", ""
    clear_button.click(fn=clear_action, inputs=[], outputs=[text_input, text_output])

if __name__ == "__main__":
    demo.launch()
