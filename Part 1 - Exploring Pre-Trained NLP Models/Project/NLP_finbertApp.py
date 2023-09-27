import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from transformers import pipeline
from datasets import load_dataset

# Create a sentiment analysis pipeline
finbert = pipeline("text-classification", model="ProsusAI/finbert")

# Function to perform sentiment analysis and update the log
def analyze_sentiment():
    text = text_entry.get("1.0", "end-1c")  # Get text from the input field
    results = finbert(text)
    
    # Display the results in the GUI
    result_text.config(text=f"Sentiment: {results[0]['label']}, Score: {results[0]['score']:.4f}")
    
    # Append the input and results to the log
    log_tree.insert("", "end", values=(text, results[0]['label'], f"{results[0]['score']:.4f}"))

# Create the main window
root = tk.Tk()
root.title("Financial Sentiment Analysis")
root.geometry("600x400")  # Set the initial size of the window

# Create and configure input text field
text_label = tk.Label(root, text="Enter a financial related text for sentiment analysis:")
text_label.pack()
text_entry = tk.Text(root, height=5, width=60)
text_entry.pack()

# Create a button to perform sentiment analysis
analyze_button = tk.Button(root, text="Analyze Sentiment", command=analyze_sentiment)
analyze_button.pack()

# Create a label to display the current sentiment analysis result
result_text = tk.Label(root, text="", wraplength=400, justify="center")
result_text.pack()

# Add a title for the log section
previous_searches_label = tk.Label(root, text="Previous Searches")
previous_searches_label.pack()

# Create a treeview widget to display the log as a table
log_tree = ttk.Treeview(root, columns=("Text", "Label", "Score"), show="headings")
log_tree.heading("Text", text="Text")
log_tree.heading("Label", text="Label")
log_tree.heading("Score", text="Score")
log_tree.pack()

# Start the Tkinter main loop
root.mainloop()