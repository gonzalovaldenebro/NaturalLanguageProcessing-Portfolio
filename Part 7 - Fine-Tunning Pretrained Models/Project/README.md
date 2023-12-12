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

<img src="https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/main/Part%205%20-%20Neural%20Network%20for%20NLP/Project/Images/InitialPage.png" alt="Alt text" width="600"/>

2. Predict: Click this button to initiate the classification of the input text.

<img src="https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/main/Part%205%20-%20Neural%20Network%20for%20NLP/Project/Images/Predict.png" alt="Alt text" width="600"/>

3. Predicted Category: This section displays the predicted category for the input text.

In this case, thhe model predicted "Sci/Tech" as the category with the highest probability (43%), but it also assigned a lower probability (0.80%) to the "Business" category. This could be due to the fact that the text may contain some technical or technology-related terms that the model associated with the "Sci/Tech" category, even though the overall context may be more relevant to "Business."

<img src="https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/main/Part%205%20-%20Neural%20Network%20for%20NLP/Project/Images/prediction%20.png" alt="Alt text" width="600"/>

## Model
The application uses a pre-trained neural network model for text classification. The model was trained on a the [ag_news dataset](https://huggingface.co/datasets/ag_news/viewer/default/train?p=4&row=442) with predefined categories.

The model's highest archievement on test data was 91.1% accurary




# Medical Question Answering Chatbot

This Python application provides a simple graphical user interface (GUI) for a medical question-answering chatbot. The chatbot utilizes the Hugging Face Transformers library and is powered by the "GonzaloValdenebro/MedicalQuestionAnswering" model checkpoint.

## Overview
The Medical Question Answering Chatbot allows users to input a medical context and ask questions related to the given context. The chatbot then utilizes a pre-trained model to provide relevant answers based on the input question and context.

## Features
Question answering in a medical context.
Utilizes a pre-trained neural network for medical question answering.
Provides answers based on user-inputted context and question.
Getting Started
Follow these steps to run the chatbot on your local machine.

## Prerequisites
Make sure you have the required libraries installed. You can install them using pip:

```bash
pip install transformers
```

## Installation
1. Clone this repository to your local machine or download the source code.
2. Open a terminal or command prompt.
3. Navigate to the application directory.

## Usage
Run the chatbot application by executing the following command:

```bash
python medical_chatbot_app.py
```
Upon running the application, a graphical user interface (GUI) window will open, featuring the following sections:

### Enter Context: Input the medical context in the provided text box.

<img src="https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/main/Part%205%20-%20Neural%20Network%20for%20NLP/Project/Images/InitialPage.png" alt="Alt text" width="600"/>

### Enter Question: Enter your medical-related question in the designated entry box.

<img src="https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/main/Part%205%20-%20Neural%20Network%20for%20NLP/Project/Images/InitialPage.png" alt="Alt text" width="600"/>

### Ask: Click this button to initiate the question-answering process.

<img src="https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/main/Part%205%20-%20Neural%20Network%20for%20NLP/Project/Images/InitialPage.png" alt="Alt text" width="600"/>

### Answer: The chatbot will display the answer based on the provided context and question.

<img src="https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/main/Part%205%20-%20Neural%20Network%20for%20NLP/Project/Images/InitialPage.png" alt="Alt text" width="600"/>

## Exiting the Chatbot
To exit the chatbot, simply input "exit" in the medical context entry, and the application will close.

## Model
The chatbot utilizes the "GonzaloValdenebro/MedicalQuestionAnswering" model checkpoint from the Hugging Face Transformers library. This model has been fine-tuned on medical question-answering tasks and aims to provide accurate and context-aware answers.

Feel free to explore and interact with the chatbot to get answers to your medical questions!
