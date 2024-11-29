# -*- coding: utf-8 -*-
"""Text classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16V7KMUBr3J4ZeTBt8dN0mZHGEoK6h6D4
"""

# Step 1: Install the necessary library
!pip install transformers

# Step 2: Import the necessary modules
from transformers import pipeline

# Step 3: Create a sentiment analysis pipeline
sentiment_analysis = pipeline(task="sentiment-analysis")

# Step 4: Define the text you want to classify
texts = [
    "I love this product! It's amazing.",
    "I'm not happy with the service I received.",
    "It's okay, not the best experience, but not the worst either."
]

# Step 5: Perform sentiment analysis on the text
results = sentiment_analysis(texts)

# Step 6: Display the results
for text, result in zip(texts, results):
    print(f"Text: {text}\nSentiment: {result['label']}, Score: {result['score']:.2f}\n")

