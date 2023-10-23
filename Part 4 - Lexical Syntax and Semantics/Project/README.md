# POS Tagging Application
This Python application provides a graphical user interface (GUI) for part-of-speech (POS) tagging of text using the BERT-based model from AdapterHub. It allows users to input text and interactively assign POS tags to words, as well as view the model's analysis of the input text.

## Introduction
This project is designed to help users perform POS tagging on text using a pre-trained BERT-based model. It offers a user-friendly interface for tagging words with their respective parts of speech and visualizing the results in a colored format.

## Usage

### 1. Running the Application
To run the application, execute the provided Python script:

```python
python pos_tagging_app.py
```

### 2. Application GUI
Upon running the script, a GUI window will open. The interface is divided into several sections:

##### 2.1. User Input: You can enter the text you want to analyze in the provided text box.

##### 2.2. Tag Input Text: Click this button to initiate tagging of the input text.

##### 2.3. Clear All: Click this button to clear all tagged words and start over.

##### 2.4. Tagged Words: This section displays the tagged words in the format word (POS). The words are color-coded based on their part of speech.

### 3. Tagging Words
Enter your text in the "User Input" box.

<img src="https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/main/Part%204%20-%20Lexical%20Syntax%20and%20Semantics/Project/Images/2.png" alt="Alt text" width="600"/>

### 4. Tagging Words
Click the "Tag Input Text" button.
For each word, you can choose a part of speech from a dropdown and click "Tag Word" to assign a tag.

<img src="https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/main/Part%204%20-%20Lexical%20Syntax%20and%20Semantics/Project/Images/3.png" alt="Alt text" width="600"/>

#### 5. Analyzing Text
After tagging words, you can click the "Compare" button to view the model's analysis of the input text. The colored text represents different POS tags.

<img src="https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/main/Part%204%20-%20Lexical%20Syntax%20and%20Semantics/Project/Images/5.png" alt="Alt text" width="600"/>

### 6. Clearing Data
If you want to start over, you can click the "Clear All" button to clear all data and tagged words.



## Installation
Before running the application, ensure you have the required libraries installed. You can install them using pip:

```python
pip install tkinter requests
```

## Acknowledgments
This project utilizes the AdapterHub's BERT-based model for POS tagging. Thanks to the AdapterHub community for providing this valuable resource.