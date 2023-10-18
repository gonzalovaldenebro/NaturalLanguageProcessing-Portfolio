# Translation and Tokenization App

This Python application combines text translation and tokenization using the Transformers library and the Tkinter framework. It allows users to input a sentence, choose source and target languages, and get translations with tokenization and part-of-speech tagging.

## Introduction

This project leverages state-of-the-art NLP models from the Transformers library to create a user-friendly translation and tokenization tool. It offers a graphical user interface (GUI) where users can input text, select source and target languages, and view translations along with tokenization and part-of-speech tagging.

## Usage

1. Run the application by executing the provided Python script:

```python
python Multilingual_Translation_TokenizationApp.py
```
2. The GUI window will open, allowing you enter a text in the following languages: 

#### Selected languages for source and output translation

- English ("en_XX") 
- French ("zh_CN")
- Mandarin Chinesse ("fr_XX")
- Arabic (ar_AR")
- Czech ("cs_CZ")
- German ("de_DE")
- Spanish ("es_XX")
- (et_EE")
- Finnish ("fi_FI")
- Italian ("it_IT")
- Japanese ("ja_XX")
- Hindi ("hi_IN")
- (gu_IN")
- Mandarin Chinesse ("zh_CN")

#### Initial user input
<img src="https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/main/Part%203%20-%20Syntax%2C%20Parsing%2C%20and%20Linguistic%20Structures/Project/Images/1.png" alt="Alt text" width="300"/>

3. Enter financial-related text in the input field.

4. Click the "Analyze Sentiment" button to perform sentiment analysis.
  
5. The sentiment analysis result (label and score) will be displayed below the input field.

#### Model output
<img src="https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/d45d2ae37e2ac557121d29e3466b3ba83349c909/Part%201%20-%20Exploring%20Pre-Trained%20NLP%20Models/Project/Images/model_results.png" alt="Alt text" width="300"/>
  
6. Previous searches and their results will be logged in the table in the "Previous Searches" section.
  
7. You can analyze the sentiment of multiple texts and review their results in the log.

### Technologies Used

- Python
- Transformers Library
- Tkinter (for GUI)
- NLTK (Natural Language Toolkit)
- SSL (for certificate verification)

## Installation

Before running the application, ensure you have the required libraries installed. You can install them using pip:

```bash
pip install transformers
pip install nltk
