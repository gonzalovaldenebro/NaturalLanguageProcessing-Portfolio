# Text Summarization and Question Answering

## Table of Contents
### Introduction
### Installation
### Usage
#### Text Summarization
#### Question Answering
### Important Notes


### Introduction
This project presents a Python application that combines text summarization and question answering functionalities using the Transformers library and the Tkinter framework. The application enables users to input textual data, generate a summary of the text, and ask questions related to the provided text.

Text summarization and question answering are essential NLP tasks with various real-world applications, such as condensing lengthy documents and extracting information from text.

### Installation
Before using the application, ensure you have the following dependencies installed. You can install them using pip:

```python
pip install transformers
pip install tkinter
```
### Usage
Run the application by executing the provided Python script:

bash
Copy code
python your_script_name.py
Replace your_script_name.py with the actual name of your Python script.

The GUI window will open, allowing you to perform text summarization and question answering on textual data.

### Text Summarization
1. Enter or paste your text into the "Enter Text" input box.

2. Click the "Summarize" button.

3. The application will split the text into manageable chunks, summarize each chunk, and display the complete summary in the "Summary" section of the GUI.

### Question Answering
1. Enter your question in the "Ask a question about the data" input box.

2. Click the "Submit" button.

3. The application will provide an answer based on the input question and the text you entered.

### Important Notes
1. For text summarization, the application uses the "facebook/bart-large-cnn" model from the Transformers library.
2. For question answering, the application uses the "deepset/roberta-base-squad2" model from the Transformers library.
3. The maximum token length supported by the summarization model is 1024 tokens. If your text exceeds this limit, it will be split into chunks for summarization.
4. The application's GUI is relatively simple and may be further customized or enhanced based on your preferences.

































