import requests
import io
import base64
from PIL import Image

class TrollsquadAI:

    base_url = "http://127.0.0.1:7860"

    def __init__(self):
        pass
    
    def text_to_image(self, payload):
        """send a request to the automatic 1111 api with the query parameters to create an image from text

        Args:
            payload (dict): The query parameters of the request passed to the automatic 1111 api
        """
        response = requests.post(url=f'{TrollsquadAI.base_url}/sdapi/v1/txt2img', json=payload)
        response = response.json()

        return TrollsquadAI.save_image_from_response(response)

    def image_to_image(self, payload):
        """send a request to the automatic 1111 api with the query parameters to create an image from one or many images 

        Args:
            payload (dict): The query parameters of the request passed to the automatic 1111 api
        """
        response = requests.post(url=f'{TrollsquadAI.base_url}/sdapi/v1/img2img', json=payload)
        response = response.json()

        return TrollsquadAI.save_image_from_response(response)
    
    @staticmethod
    def save_image_from_response(response):
        """save the images of the automatic 1111 api call response 

        Args:
            response (dict): response from the automatic 1111 api call
        """
        try:
            i=1
            for image in response['images']:
                image = Image.open(io.BytesIO(base64.b64decode(image)))
                image.save(f'output{i}.png')
                i+=1
            return "images created", 200
        except:
            return response, 500