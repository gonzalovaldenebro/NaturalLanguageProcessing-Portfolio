# Translation and Tokenization App

This Python application combines text translation and tokenization using the Transformers library and the Tkinter framework. It allows users to input a sentence, choose source and target languages, and get translations with tokenization and part-of-speech tagging.

## Introduction

This project leverages state-of-the-art NLP models from the Transformers library to create a user-friendly translation and tokenization tool. It offers a graphical user interface (GUI) where users can input text, select source and target languages, and view translations along with tokenization and part-of-speech tagging.

## Usage

### 1. Run the application by executing the provided Python script:

```python
python Multilingual_Translation_TokenizationApp.py
```
### 2. The GUI window will open

<img src="https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/main/Part%203%20-%20Syntax%2C%20Parsing%2C%20and%20Linguistic%20Structures/Project/Images/1.png" alt="Alt text" width="300"/>


### 3. Enter input text 

<img src="https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/main/Part%203%20-%20Syntax%2C%20Parsing%2C%20and%20Linguistic%20Structures/Project/Images/2.png" alt="Alt text" width="300"/>

### 4. Select source language

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

<img src="https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/main/Part%203%20-%20Syntax%2C%20Parsing%2C%20and%20Linguistic%20Structures/Project/Images/3.png" alt="Alt text" width="500"/>

### 4. Select one or multiple target languages

In other words, we can translate and tokenize the original (source) language to one or multiple languages by selecting the many languages we want the app to process.

<img src="https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/main/Part%203%20-%20Syntax%2C%20Parsing%2C%20and%20Linguistic%20Structures/Project/Images/4.png" alt="Alt text" width="500"/>

  
### 5. Click Translate and explore the results

Once we have selected our input text, source language, target languages we can explore the results. As listed in the example shown in the image below, we can see that it does not only translate and tokenize but it assigns a part-of-speech tagging. 

<img src="https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/main/Part%203%20-%20Syntax%2C%20Parsing%2C%20and%20Linguistic%20Structures/Project/Images/5.png" alt="Alt text" width="600"/>


## Installation

Before running the application, ensure you have the required libraries installed. You can install them using pip:

```bash
pip install transformers
pip install nltk
