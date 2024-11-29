# -*- coding: utf-8 -*-
"""Audio classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1l96yGAXfqSPn-YJM1k-WaSp2jcchf8wB
"""

# Step 1: Install the necessary libraries
!pip install transformers
!pip install torch torchaudio

# Step 2: Import the necessary modules
from transformers import pipeline
import requests

# Step 3: Create an audio classification pipeline
audio_classifier = pipeline(task="audio-classification", model="superb/wav2vec2-base-superb-ks")

# Step 4: Define the path to the local audio file
audio_path = "audio.wav"  # Ensure this file is uploaded to your Colab environment

# Step 5: Perform audio classification
results = audio_classifier(audio_path)

# Step 5: Perform audio classification
results = audio_classifier(audio_path)

# Step 6: Display the classification results
for result in results:
    print(f"Label: {result['label']}, Score: {result['score']:.2f}")

