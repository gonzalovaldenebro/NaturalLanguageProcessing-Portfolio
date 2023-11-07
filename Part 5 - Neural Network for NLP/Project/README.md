# Text Classification using Neural Networks
This Python application provides a graphical user interface (GUI) for part-of-speech (POS) tagging of text using the BERT-based model from AdapterHub. It allows users to input text and interactively assign POS tags to words, as well as view the model's analysis of the input text.

## Overview
This Python application allows users to perform text classification using a pre-trained neural network. It takes user input text and predicts its category from a predefined set of categories. The application is designed for simplicity and ease of use.

## Features
- Text classification with a pre-trained neural network.
- Predicts the category of the input text.
- Displays the predicted category and other possible categories with their prediction percentages.

## Getting Started
Follow these steps to run the application on your local machine.

### Prerequisites
Make sure you have the required libraries installed. You can install them using pip:

```bash
pip install tensorflow keras joblib
```
### Installation
1. Clone this repository to your local machine or download the source code.
2. Open a terminal or command prompt.
3. Navigate to the application directory.

### Usage
Run the application by executing the following command:

```bash
python text_classification_app.py
```

Upon running the application, a graphical user interface (GUI) window will open. The interface consists of the following sections:

1. User Input: You can enter the text you want to classify in the provided text box.

<img src="https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/main/Part%204%20-%20Lexical%20Syntax%20and%20Semantics/Project/Images/3.png" alt="Alt text" width="600"/>

2. Predict: Click this button to initiate the classification of the input text.

<img src="https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/main/Part%204%20-%20Lexical%20Syntax%20and%20Semantics/Project/Images/3.png" alt="Alt text" width="600"/>

3. Predicted Category: This section displays the predicted category for the input text.

In this case, thhe model predicted "Sci/Tech" as the category with the highest probability (43%), but it also assigned a lower probability (0.80%) to the "Business" category. This could be due to the fact that the text may contain some technical or technology-related terms that the model associated with the "Sci/Tech" category, even though the overall context may be more relevant to "Business."

<img src="https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/main/Part%204%20-%20Lexical%20Syntax%20and%20Semantics/Project/Images/3.png" alt="Alt text" width="600"/>


## Model
The application uses a pre-trained neural network model for text classification. The model was trained on a the [ag_news dataset](https://huggingface.co/datasets/ag_news/viewer/default/train?p=4&row=442) with predefined categories.























