import tkinter as tk
from transformers import pipeline

# Create a summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Create a question-answering pipeline
model_name = "deepset/roberta-base-squad2"
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

def summarize_text():
    text = text_box.get("1.0", "end-1c")  # Get the text from the input box
    max_chunk_length = 1024  # Maximum token length supported by the model
    chunks = [text[i:i + max_chunk_length] for i in range(0, len(text), max_chunk_length)]
    summaries = []

    for chunk in chunks:
        summary = summarizer(chunk)[0]['summary_text']
        summaries.append(summary)

    summary = " ".join(summaries)

    # Display the summary in the GUI
    summary_text.config(state="normal")  # Enable text widget for editing
    summary_text.delete("1.0", "end")  # Clear previous content
    summary_text.insert("1.0", summary)  # Insert the summary
    summary_text.config(state="disabled")  # Disable text widget for editing

def answer_question():
    question = question_entry.get()
    context = text_box.get("1.0", "end-1c")
    response = nlp(question=question, context=context)
    answer_label.config(text=response['answer'])

# Create the main window
root = tk.Tk()
root.title("Text Summarization and Question Answering")

# Create a text input box
text_label = tk.Label(root, text="Enter Text:")
text_label.pack()
text_box = tk.Text(root, width=80, height=20)  # Increase width and height
text_box.pack()

# Create a button to summarize text
summarize_button = tk.Button(root, text="Summarize", command=summarize_text)
summarize_button.pack()

# Create a label to display the summary
summary_label = tk.Label(root, text="Summary:")
summary_label.pack()
summary_text = tk.Text(root, width=80, height=20, state="disabled")  # Increase width and height
summary_text.pack()

# Create a label for the question input
question_label = tk.Label(root, text="Ask a question about the data:")
question_label.pack()

# Create an entry box for asking questions
question_entry = tk.Entry(root, width=60)
question_entry.pack()

# Create a button to answer questions
answer_button = tk.Button(root, text="Submit", command=answer_question)
answer_button.pack()

# Create a label to display the answer
answer_label = tk.Label(root, text="")
answer_label.pack()

# Start the main loop
root.mainloop()
