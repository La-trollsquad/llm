import requests
import io
import base64
from PIL import Image

class TrollsquadAI:
    def __init__(self):
        pass

    def text_to_image(self, payload):

        response = requests.post(url='http://127.0.0.1:7860/sdapi/v1/txt2img', json=payload)
        response = response.json()

        return TrollsquadAI.save_image_from_response(response)

    def image_to_image(self, payload):

        with open("black and white trollface.png", 'rb') as file:
            image_data = file.read()
            encoded_image = base64.b64encode(image_data).decode('utf-8')
        payload['init_images']=[encoded_image]
        response = requests.post(url='http://127.0.0.1:7860/sdapi/v1/img2img', json=payload)
        response = response.json()

        return TrollsquadAI.save_image_from_response(response)
    
    @staticmethod
    def save_image_from_response(response):
        try:
            i=1
            for image in response['images']:
                image = Image.open(io.BytesIO(base64.b64decode(image)))
                image.save(f'output{i}.png')
                i+=1
            return "images created", 200
        except:
            return response, 500