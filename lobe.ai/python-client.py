# !cat mask.jpg | base64
# !base64 mask.jpg
# !base64 mask.jpg

import requests
import base64

url = "http://127.0.0.1:38100/predict/dbe05db58b43"
 
def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')
