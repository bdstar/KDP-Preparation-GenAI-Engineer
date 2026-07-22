# A vision-capable model reads an image alongside a text question.
import base64
 
with open("invoice_scan.png", "rb") as f:
    image_b64 = base64.standard_b64encode(f.read()).decode()
 
response = call_multimodal_model(messages=[{
    "role": "user",
    "content": [
        {"type": "text", "text": "What is the total amount due on this invoice?"},
        {"type": "image", "source": {"type": "base64", "media_type": "image/png",
                                      "data": image_b64}},
    ],
}])
# The model reads the invoice image — including its table — and answers in text.
