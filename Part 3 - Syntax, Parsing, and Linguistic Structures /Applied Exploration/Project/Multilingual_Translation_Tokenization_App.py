import tkinter as tk
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
from nltk import word_tokenize, pos_tag
import nltk
import ssl

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# Download NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Load the model and tokenizer
model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")

# Define a list of available languages
languages = ["en_XX", "fr_XX", "ar_AR", "cs_CZ", "de_DE", "es_XX", "et_EE", "fi_FI", "gu_IN", "hi_IN", "it_IT", "ja_XX", "zh_CN"]

# Initialize a flag to check if source input is already displayed
source_input_displayed = False

def translate_and_display():
    global source_input_displayed
    user_input_text = user_input.get()
    src_lang = source_lang_var.get()
    target_languages = [target_lang_list.get(idx) for idx in target_lang_list.curselection()]

    # Set the source language
    tokenizer.src_lang = src_lang

    # Encode the user input
    encoded_input = tokenizer(user_input_text, return_tensors="pt")

    # Clear previous output
    output_text.delete(1.0, tk.END)

    # Display source input only if it's not displayed yet
    if not source_input_displayed:
        output_text.insert(tk.END, f"Source Input ({src_lang}):\n{user_input_text}\n\n")
        source_input_displayed = True

    # Generate translations for selected target languages
    for target_language in target_languages:
        generated_tokens = model.generate(
            **encoded_input,
            forced_bos_token_id=tokenizer.lang_code_to_id[target_language]
        )

        # Decode the translation
        translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]

        # Tokenize the source and translation using NLTK
        source_tokens = word_tokenize(user_input_text)
        translation_tokens = word_tokenize(translation)

        # Perform part-of-speech tagging
        source_pos_tags = pos_tag(source_tokens)
        translation_pos_tags = pos_tag(translation_tokens)

        # Display translation and tokenization
        output_text.insert(tk.END, f"Translation to {target_language}:\n{translation}\n\n")
        output_text.insert(tk.END, f"Translation Tokenization:\n{translation_tokens}\n\n")
        output_text.insert(tk.END, f"Translation POS Tags:\n{translation_pos_tags}\n\n")

# Create a Tkinter window
window = tk.Tk()
window.title("Translation and Tokenization App")
window.geometry("800x600")

# Create and place widgets in the window
user_input_label = tk.Label(window, text="Enter the source sentence:")
user_input = tk.Entry(window)
source_lang_label = tk.Label(window, text="Source Language:")
source_lang_var = tk.StringVar()
source_lang_combobox = tk.OptionMenu(window, source_lang_var, *languages)
source_lang_var.set("en_XX")  # Default source language
target_lang_label = tk.Label(window, text="Select target languages:")
target_lang_list = tk.Listbox(window, selectmode=tk.MULTIPLE, exportselection=0)
for lang in languages:
    target_lang_list.insert(tk.END, lang)
translate_button = tk.Button(window, text="Translate", command=translate_and_display)
output_text = tk.Text(window, wrap=tk.WORD)

# Grid layout for widgets
user_input_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
user_input.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
source_lang_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
source_lang_combobox.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)
target_lang_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
target_lang_list.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)
translate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
output_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter main loop
window.mainloop()
