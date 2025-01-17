# -*- coding: utf-8 -*-
"""Image captioning.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1u_6rTrkeRuTHLmx1KAHkQBVXeaffYMnL
"""

# Step 1: Install the necessary libraries
!pip install transformers
!pip install torch torchvision
!pip install pillow

# Step 2: Import the necessary modules
from transformers import pipeline
from PIL import Image
import requests

# Step 3: Create an image-to-text pipeline
caption_pipeline = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

# Step 4: Define the image you want to caption
# You can use a URL of an image or upload an image to Colab and provide the file path
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Kittyply_edit1.jpg/1280px-Kittyply_edit1.jpg"
image = Image.open(requests.get(image_url, stream=True).raw)

# Step 5: Generate a caption for the image
result = caption_pipeline(image)

# Step 6: Display the generated caption
print("Generated Caption:", result[0]['generated_text'])

image_url = "https://images.unsplash.com/photo-1611083517823-b432dc3b7320?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
image = Image.open(requests.get(image_url, stream=True).raw)
result = caption_pipeline(image)
print("Generated Caption:", result[0]['generated_text'])

