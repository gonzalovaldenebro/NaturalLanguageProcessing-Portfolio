import tkinter as tk
from transformers import pipeline

# Replace this with your own checkpoint
model_checkpoint = "GonzaloValdenebro/MedicalQuestionAnswering"
question_answerer = pipeline("question-answering", model=model_checkpoint)

class MedicalChatbotApp:
    def __init__(self, master):
        self.master = master
        master.title("Medical Chatbot")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Hi! I'm a medical question answering chatbot.")
        self.label.pack()

        self.context_entry_label = tk.Label(self.master, text="Enter Context:")
        self.context_entry_label.pack()

        # Use tk.Text for a larger, multiline entry box
        self.context_entry = tk.Text(self.master, width=50, height=5)
        self.context_entry.pack()

        self.question_entry_label = tk.Label(self.master, text="Enter Question:")
        self.question_entry_label.pack()

        self.question_entry = tk.Entry(self.master, width=50)
        self.question_entry.pack()

        self.answer_label = tk.Label(self.master, text="")
        self.answer_label.pack()

        self.ask_button = tk.Button(self.master, text="Ask", command=self.ask_question)
        self.ask_button.pack()

        self.exit_button = tk.Button(self.master, text="Exit", command=self.master.quit)
        self.exit_button.pack()

    def ask_question(self):
        user_context = self.context_entry.get("1.0", tk.END).strip()  # Get text from the Text widget
        user_question = self.question_entry.get()

        if user_context.lower() == 'exit':
            self.master.quit()

        answer = question_answerer(question=user_question, context=user_context)
        self.answer_label.config(text=f"Answer: {answer['answer']}")

def main():
    root = tk.Tk()
    app = MedicalChatbotApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
