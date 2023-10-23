import tkinter as tk
from tkinter import scrolledtext, StringVar, OptionMenu, Button, Scrollbar, Canvas, Frame, Entry
import requests

API_URL = "https://api-inference.huggingface.co/models/AdapterHub/bert-base-uncased-pf-ud_pos"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Store the user-assigned tags for each word
user_tags = {}

# Clear any previous tags from the previous run
user_tags.clear()

# Define the part-of-speech color map
pos_color_map = {
    "NOUN": "green",
    "PUNCT": "blue",
    "ADP": "cyan",
    "NUM": "magenta",
    "SYM": "yellow",
    "SCONJ": "red",
    "ADJ": "orange",
    "PART": "purple",
    "DET": "brown",
    "CCONJ": "pink",
    "PROPN": "violet",
    "PRON": "gray",
    "X": "olive",
    "_": "lime",
    "ADV": "coral",
    "INTJ": "gold",
    "VERB": "orchid",
    "AUX": "navy",
}

# Callback for tagging input text
def tag_input_text():
    user_input_text = user_input.get("1.0", tk.END).strip()
    user_input_words = user_input_text.split()

    for word in user_input_words:
        word = word.strip()
        if word:
            selected_tag = StringVar(tagging_frame)
            selected_tag.set("NOUN")  # Default tag
            word_frame = Frame(word_boxes_frame)
            word_frame.pack(side="top", fill="x")
            word_box = Entry(word_frame, font=("Arial", 14))
            word_box.insert(0, word)
            word_box.pack(side="left")
            tag_dropdown = OptionMenu(word_frame, selected_tag, *pos_color_map.keys())
            tag_dropdown.config(font=("Arial", 12))
            tag_dropdown.pack(side="left")
            tag_button = Button(word_frame, text="Tag Word", command=lambda w=word, t=selected_tag: tag_word(w, t), font=("Arial", 12))
            tag_button.pack(side="left")
            word_boxes.append((word, word_box, selected_tag, tag_button))
    
    compare_button.config(state="normal")
    tag_input_button.config(state="disabled")

# Callback for tagging a specific word
def tag_word(word, selected_tag):
    tag = selected_tag.get()
    if tag:
        user_tags[word] = (tag, pos_color_map[tag])
        refresh_tagged_words()

# Refresh the tagged words display
def refresh_tagged_words():
    tagged_words.config(state="normal")
    tagged_words.delete("1.0", tk.END)
    for word, (tag, color) in user_tags.items():
        tagged_words.insert(tk.END, f"{word} ({tag})\n")
        tagged_words.tag_config(f"{tag}", foreground=color)
    tagged_words.config(state="disabled")

# Callback for analyzing and comparing text
def analyze_and_compare_text():
    # Clear the previous analysis
    colored_text.config(state="normal")
    colored_text.delete("1.0", tk.END)
    
    user_input_text = user_input.get("1.0", tk.END).strip()
    user_input_words = user_input_text.split()

    # Display the model's analysis
    model_analysis = "Model's Analysis:\n"

    # Assuming the model response is a JSON string, otherwise display it as is
    try:
        for token in query({"inputs": user_input_text}):
            word = token.get('word', '')
            pos = token.get('entity_group', '')
            tag_color = pos_color_map.get(pos, "black")
            model_analysis += f"{word} ({pos}) "
    except ValueError:
        model_analysis = user_input_text

    colored_text.insert("1.0", model_analysis, "model_tag")
    colored_text.tag_add("model_tag", "1.0", "end")
    colored_text.tag_config("model_tag", foreground=tag_color)
    colored_text.config(state="disabled")

# Callback for clearing all data
def clear_all():
    for word, _, _, _ in word_boxes:
        user_tags.pop(word, None)
    word_boxes.clear()
    user_input.delete("1.0", tk.END)
    tagged_words.config(state="normal")
    tagged_words.delete("1.0", tk.END)
    tagged_words.config(state="disabled")
    colored_text.config(state="normal")
    colored_text.delete("1.0", tk.END)
    colored_text.config(state="disabled")
    tag_input_button.config(state="normal")
    compare_button.config(state="disabled")

# Create the main window
window = tk.Tk()
window.title("POS Tag Analyzer")
window.geometry("800x600")

# Create a frame for user tagging
tagging_frame = tk.Frame(window, padx=10, pady=10)
tagging_frame.pack(side="top", fill="both")

# Create a frame for input and word boxes
input_frame = tk.Frame(tagging_frame)
input_frame.pack(side="left")

# Create a scrolled text widget for user input
user_input = scrolledtext.ScrolledText(input_frame, wrap="none", font=("Arial", 14), width=40, height=5)
user_input.pack()

# Create a "Tag Input Text" button
tag_input_button = Button(tagging_frame, text="Tag Input Text", command=tag_input_text, font=("Arial", 14))
tag_input_button.pack()

# Create a "Clear All" button
clear_button = Button(tagging_frame, text="Clear All", command=clear_all, font=("Arial", 14))
clear_button.pack()

# Create a frame for word boxes
word_boxes_frame = tk.Frame(tagging_frame)
word_boxes_frame.pack(side="left")

word_boxes = []

# Create a "Compare" button (initially disabled)
compare_button = Button(tagging_frame, text="Compare", command=analyze_and_compare_text, font=("Arial", 14), state="disabled")
compare_button.pack()

# Create a canvas for tagged words with scrollbar
canvas = Canvas(window)
canvas.pack(side="left", fill="both", expand=True)

# Create a frame for displaying tagged words
tagged_words_frame = Frame(canvas)
canvas.create_window((0, 0), window=tagged_words_frame, anchor="nw")

tagged_words = scrolledtext.ScrolledText(tagged_words_frame, wrap="none", font=("Arial", 14), width=45)
tagged_words.pack(fill="both", expand=True)

# Bind the canvas to the frame size
tagged_words_frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

# Create a canvas for colored text with scrollbar
colored_text_canvas = Canvas(window)
colored_text_canvas.pack(side="left", fill="both", expand=True)

# Create a frame for displaying colored output
colored_text_frame = Frame(colored_text_canvas)
colored_text_canvas.create_window((0, 0), window=colored_text_frame, anchor="nw")

colored_text = scrolledtext.ScrolledText(colored_text_frame, wrap="none", font=("Arial", 14), width=45)
colored_text.pack(fill="both", expand=True)

# Bind the canvas to the frame size
colored_text_frame.bind("<Configure>", lambda event, canvas=colored_text_canvas: colored_text_canvas.configure(scrollregion=canvas.bbox("all")))

# Start the tkinter main loop
window.mainloop()
