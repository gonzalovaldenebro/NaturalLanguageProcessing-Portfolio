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

<img src="https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/main/Part%207%20-%20Fine-Tunning%20Pretrained%20Models/Project/Images/Image1.png" alt="Alt text" width="600"/>

### Enter Question: Enter your medical-related question in the designated entry box.

<img src="https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/main/Part%207%20-%20Fine-Tunning%20Pretrained%20Models/Project/Images/Image2.png" alt="Alt text" width="600"/>

### Ask: Click this button to initiate the question-answering process.

<img src="https://github.com/gonzalovaldenebro/NaturalLanguageProcessing-Portfolio/blob/main/Part%207%20-%20Fine-Tunning%20Pretrained%20Models/Project/Images/Image3.png" alt="Alt text" width="600"/>

### Answer: The chatbot will display the answer based on the provided context and question.

## Exiting the Chatbot
To exit the chatbot, simply input "exit" in the medical context entry, and the application will close.

## Model
The chatbot utilizes the "GonzaloValdenebro/MedicalQuestionAnswering" model checkpoint from the Hugging Face Transformers library. This model has been fine-tuned on medical question-answering tasks and aims to provide accurate and context-aware answers.

Feel free to explore and interact with the chatbot to get answers to your medical questions!
