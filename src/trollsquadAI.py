import os
import replicate
from dotenv import load_dotenv

class TrollsquadAI:

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

        string_dialogue = f"Titre: {prompt} --- Rédiges ce titre en une petite histoire, ta réponse dois seulement contenir l'histoire absolument dans la langue Française qui donne le contexte sans répéter le titre et sans moral."

        output = replicate.run(llm,
                               input={"prompt": string_dialogue,
                                      "temperature": temperature, "top_p": top_p, "max_length": max_length,
                                      "repetition_penalty": repetition_penalty})

        return output