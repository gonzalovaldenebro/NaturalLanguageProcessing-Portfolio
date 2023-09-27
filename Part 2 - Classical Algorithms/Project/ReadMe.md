# Text Summarization and Question Answering

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

```python
python QA_SummarizerGUIApp.py
```
The GUI window will open, allowing you to perform text summarization and question answering on textual data.

### Text Summarization
1. Enter or paste your text into the "Enter Text" input box.
<img src="[https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/891ab96f1771ea2df45b680e04439024d2d14d30/Part%201%20-%20Exploring%20Pre-Trained%20NLP%20Models/Project/Images/user_input.png](https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/b27d5ffc306a0012dae1e15db81a5144b80687bd/Part%202%20-%20Classical%20Algorithms/Project/Screenshot%202023-09-27%20at%2014.39.19.png)" alt="Alt text" width="300"/>

2. Click the "Summarize" button.

<img src="(https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/b27d5ffc306a0012dae1e15db81a5144b80687bd/Part%202%20-%20Classical%20Algorithms/Project/Screenshot%202023-09-27%20at%2014.41.18.png)" width="300"/>

3. The application will split the text into manageable chunks, summarize each chunk, and display the complete summary in the "Summary" section of the GUI.

<img src="[https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/891ab96f1771ea2df45b680e04439024d2d14d30/Part%201%20-%20Exploring%20Pre-Trained%20NLP%20Models/Project/Images/user_input.png](https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/b27d5ffc306a0012dae1e15db81a5144b80687bd/Part%202%20-%20Classical%20Algorithms/Project/Screenshot%202023-09-27%20at%2014.39.19.png)" alt="Alt text](https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/b27d5ffc306a0012dae1e15db81a5144b80687bd/Part%202%20-%20Classical%20Algorithms/Project/Screenshot%202023-09-27%20at%2014.41.18.png)](https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/b27d5ffc306a0012dae1e15db81a5144b80687bd/Part%202%20-%20Classical%20Algorithms/Project/Screenshot%202023-09-27%20at%2014.42.07.png)" width="300"/>

### Question Answering
1. Enter your question in the "Ask a question about the data" input box.

<img src="[https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/891ab96f1771ea2df45b680e04439024d2d14d30/Part%201%20-%20Exploring%20Pre-Trained%20NLP%20Models/Project/Images/user_input.png](https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/b27d5ffc306a0012dae1e15db81a5144b80687bd/Part%202%20-%20Classical%20Algorithms/Project/Screenshot%202023-09-27%20at%2014.39.19.png)" alt="Alt text](https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/b27d5ffc306a0012dae1e15db81a5144b80687bd/Part%202%20-%20Classical%20Algorithms/Project/Screenshot%202023-09-27%20at%2014.41.18.png)](https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/b27d5ffc306a0012dae1e15db81a5144b80687bd/Part%202%20-%20Classical%20Algorithms/Project/Screenshot%202023-09-27%20at%2014.42.07.png)](https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/b27d5ffc306a0012dae1e15db81a5144b80687bd/Part%202%20-%20Classical%20Algorithms/Project/Screenshot%202023-09-27%20at%2014.42.37.png)" width="300"/>

2. Click the "Submit" button.

3. The application will provide an answer based on the input question and the text you entered.
<img src="[https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/891ab96f1771ea2df45b680e04439024d2d14d30/Part%201%20-%20Exploring%20Pre-Trained%20NLP%20Models/Project/Images/user_input.png](https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/b27d5ffc306a0012dae1e15db81a5144b80687bd/Part%202%20-%20Classical%20Algorithms/Project/Screenshot%202023-09-27%20at%2014.39.19.png)" alt="Alt text](https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/b27d5ffc306a0012dae1e15db81a5144b80687bd/Part%202%20-%20Classical%20Algorithms/Project/Screenshot%202023-09-27%20at%2014.41.18.png)](https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/b27d5ffc306a0012dae1e15db81a5144b80687bd/Part%202%20-%20Classical%20Algorithms/Project/Screenshot%202023-09-27%20at%2014.42.07.png)](https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/b27d5ffc306a0012dae1e15db81a5144b80687bd/Part%202%20-%20Classical%20Algorithms/Project/Screenshot%202023-09-27%20at%2014.42.37.png)](https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/b27d5ffc306a0012dae1e15db81a5144b80687bd/Part%202%20-%20Classical%20Algorithms/Project/Screenshot%202023-09-27%20at%2014.43.02.png)" width="300"/>
 

### Important Notes
1. For text summarization, the application uses the "facebook/bart-large-cnn" model from the Transformers library.
2. For question answering, the application uses the "deepset/roberta-base-squad2" model from the Transformers library.
3. The maximum token length supported by the summarization model is 1024 tokens. If your text exceeds this limit, it will be split into chunks for summarization.
4. The application's GUI is relatively simple and may be further customized or enhanced based on your preferences.

































