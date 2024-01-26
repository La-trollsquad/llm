import os
import io
import base64
import requests
import replicate
from PIL import Image
from dotenv import load_dotenv
from transformers import MarianMTModel, MarianTokenizer

class TrollsquadAI:

    base_url = "http://127.0.0.1:7860"
    
    def __init__(self):
        pass
    
    def prompt_to_text(self, prompt):
        """
        Setup llama 2 parameters and start generating the response

        Args:
            prompt (str): The user's input prompt.
        """
    
        load_dotenv()
        replicate_api = os.getenv('REPLICATE_API_TOKEN')

        if replicate_api is None or not (replicate_api.startswith('r8_') and len(replicate_api) == 40):
            return "Please provide valid Replicate API credentials.", 400

        # paramètres
        selected_model = 'Llama2-13B'
        llm = 'a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5'
        temperature = 0.72
        top_p = 0.73   
        max_length = 1000
        repetition_penalty = 1

        return self.generate_llama2_response(llm, prompt, temperature, top_p, max_length, repetition_penalty) 

    def generate_llama2_response(self, llm, prompt, temperature, top_p, max_length, repetition_penalty):
        """
        Generates a response using the Llama2 chatbot based on the provided prompt.
        
        Args:
            replicate_api (str): replicate API token
            llm (str): llama2 model identifier
            prompt (str)
            temperature (float)
            top_p (float): Top-p parameter for Llama2
            max_length (int): Maximum length for the generated response
        """

        output = replicate.run(llm,
                               input={"prompt": prompt,
                                      "temperature": temperature, "top_p": top_p, "max_length": max_length,
                                      "repetition_penalty": repetition_penalty})

        return output
      
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
    
    def helsinki_translator(self, prompt, langSource, langTarget):
        """translate the prompt with helsinki

        Args:
            prompt (str) : text to translate
        """
        model_id = f"Helsinki-NLP/opus-mt-{langSource}-{langTarget}"
        tokenizer = MarianTokenizer.from_pretrained(model_id)

        model = MarianMTModel.from_pretrained(model_id)

        src_text = str(prompt)
        translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))
        res = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]

        return res[0]
    
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


