import requests
import io
import base64
from PIL import Image

class TrollsquadAI:
    def __init__(self):
        pass

    def text_to_image(self, payload):

        response = requests.post(url=f'http://127.0.0.1:7860/sdapi/v1/txt2img', json=payload)
        response = response.json()

        try:
            image = Image.open(io.BytesIO(base64.b64decode(response['images'][0])))
            image.save("output.png")
            return True
        except:
            return response


    def image_to_image(self, image_path):
        payload = {
            "prompt": image_path,
            "steps": 5
        }
        response = requests.post(url=f'http://127.0.0.1:7860/sdapi/v1/img2img', json=payload)
        response = response.json()
        image = Image.open(io.BytesIO(base64.b64decode(response['images'][0])))
        image.save(output_path)