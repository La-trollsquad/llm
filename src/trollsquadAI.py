import os
import replicate

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
        os.environ['REPLICATE_API_TOKEN'] = 'r8_EumTGGkohLlx9R8V5mfdTVbZaUVFIxS4FFN7p'
        replicate_api = os.getenv('REPLICATE_API_TOKEN')

        if replicate_api is None or not (replicate_api.startswith('r8_') and len(replicate_api) == 40):
            return "Please provide valid Replicate API credentials.", 400

        # paramètres
        selected_model = 'Llama2-13B'
        llm = 'a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5'
        temperature = 0.1
        top_p = 0.9
        max_length = 200

        return self.generate_llama2_response(replicate_api, llm, prompt, temperature, top_p, max_length) 

    def generate_llama2_response(self, replicate_api, llm, prompt, temperature, top_p, max_length):
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

        string_dialogue = f"Transformes ce titre en une petite histoire, réponds seulement avec l'histoire et parle en français. Le titre est : {prompt}"

        output = replicate.run(llm,
                               input={"prompt": string_dialogue,
                                      "temperature": temperature, "top_p": top_p, "max_length": max_length,
                                      "repetition_penalty": 1})

        return output
