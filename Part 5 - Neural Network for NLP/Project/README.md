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



2. Predict: Click this button to initiate the classification of the input text.



3. Predicted Category: This section displays the predicted category for the input text.



## Model
The application uses a pre-trained neural network model for text classification. The model was trained on a the [ag_news dataset](https://huggingface.co/datasets/ag_news/viewer/default/train?p=4&row=442) with predefined categories.























