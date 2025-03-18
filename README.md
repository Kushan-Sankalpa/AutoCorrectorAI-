

---

# Autocorrector-AI / Spell Checker Tool

Autocorrector-AI is an advanced grammar and spell correction tool that uses a fine-tuned T5 model to generate corrected text from user input. This AI leverages state-of-the-art deep learning techniques to fix spelling mistakes and correct grammatical errors, making it far more effective than traditional rule-based systems.

The project features an interactive web interface built with [Gradio](https://gradio.app/), so you can easily type or paste text, get corrections in real time, and clear the interface for new inputs.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Example](#example)
- [Contact](#contact)

---

## Overview

Autocorrector-AI is designed to help you improve your writing by automatically correcting spelling and grammar errors. It uses the T5 model—specifically the `vennify/t5-base-grammar-correction` variant—which has been fine-tuned for grammar correction tasks. This allows the model to understand context and provide natural, human-like corrections.

---

## Features

- **Grammar and Spell Correction:** Fixes common spelling mistakes and grammatical errors.
- **Interactive Web Interface:** A simple and responsive UI built using Gradio.
- **Clear Functionality:** Easily reset the input and output fields.
- **User-Friendly:** Just type your text, click a button, and receive corrected output.

---

## Dependencies

The project requires the following libraries:

- **Python 3.7+**
- **Gradio:** For building the web interface.
- **Transformers:** For loading and using the T5 model.
- **PyTorch:** As the deep learning framework backend for the T5 model.

Install these dependencies via pip:

```bash
pip install gradio transformers torch
```

---

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/Autocorrector-AI.git
   cd Autocorrector-AI
   ```


2. **Install the Required Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   *(Alternatively, you can manually install using the pip command shown in the Dependencies section.)*

---

## Usage

To launch the web interface, run the following command in your project directory:

```bash
python app_gradio.py
```

This command will start a local web server. Open the provided URL (e.g., `http://127.0.0.1:7860`) in your browser to interact with the autocorrect tool.

---

## How It Works

1. **User Input:**  
   You enter a sentence (which may contain spelling or grammar mistakes) in the input textbox.

2. **Processing:**  
   The T5-based model processes the text using a text-to-text generation pipeline from the Transformers library. It corrects errors by understanding the context of the sentence.

3. **Output:**  
   The corrected sentence is displayed in the output textbox.

4. **Clear Functionality:**  
   A clear button is provided to reset both input and output fields for new corrections.

---

## Example

**Input:**  
```
I cant beleive how gud this is.
```

**Expected Output:**  
```
I can't believe how good this is.
```

**Input:**  
```
She dont like going there.
```

**Expected Output:**  
```
She doesn't like going there.

```

Test the tool with various sentences to see how it handles different types of errors.

---

## Contributing

Contributions are welcome! If you have suggestions, improvements, or bug fixes, please open an issue or submit a pull request.

---

## Contact

For any questions or feedback, please contact:

- **Name:** Kushan Sankalpa
- **Email:** kushansankalpa717@gmail.com

---

Enjoy using Autocorrector-AI and happy writing!

---

