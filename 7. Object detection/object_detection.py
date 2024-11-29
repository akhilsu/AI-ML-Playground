# -*- coding: utf-8 -*-
"""Object detection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1q4x7Sb-2esqZdsyhb7gHkHNYuIzvd4vM
"""

# Step 1: Install the necessary libraries
!pip install transformers
!pip install torch torchvision
!pip install pillow

# Step 2: Import the necessary modules
from transformers import pipeline
from PIL import Image
import requests
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Step 3: Create an object detection pipeline
object_detector = pipeline(task="object-detection")

# Step 4: Define the image you want to detect objects in
image_url = "https://easy-peasy.ai/cdn-cgi/image/quality=80,format=auto,width=700/https://fdczvxmwwjwpwbeeqcth.supabase.co/storage/v1/object/public/images/a8bf1a2c-259e-4e95-b2c2-bb995876ed63/a252bcd6-9a10-40be-bf99-1d850d2026e4.png"
image = Image.open(requests.get(image_url, stream=True).raw)

# Step 5: Perform object detection
results = object_detector(image)

# Step 6: Display the detection results
plt.figure(figsize=(10, 10))
plt.imshow(image)
plt.axis('off')

# Create a Rectangle patch for each detected object
ax = plt.gca()
for result in results:
    box = result['box']
    label = result['label']
    score = result['score']

    # Draw the bounding box
    rect = patches.Rectangle((box['xmin'], box['ymin']), box['xmax'] - box['xmin'], box['ymax'] - box['ymin'],
                             linewidth=2, edgecolor='r', facecolor='none')
    ax.add_patch(rect)

    # Add the label and score
    plt.text(box['xmin'], box['ymin'], f"{label}: {score:.2f}", color='red', fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

plt.show()
