from transformers import pipeline
from PIL import Image

# Create a captioner pipeline using a pre‑trained image captioning model
captioner = pipeline(
    "image-to-text",
    model="Salesforce/blip-image-captioning-base"
)

# Load the image you want to caption
img = Image.open("your_image.jpg")

# Generate caption(s)
captions = captioner(img)

# Display results
for i, cap in enumerate(captions):
    print(f"Caption {i + 1}: {cap['generated_text']}")
