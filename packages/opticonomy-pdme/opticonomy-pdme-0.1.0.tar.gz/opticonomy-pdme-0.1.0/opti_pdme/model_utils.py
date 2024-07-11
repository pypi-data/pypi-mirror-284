from langchain_openai import ChatOpenAI
from huggingface_hub import login
from transformers import AutoModelForCausalLM, AutoTokenizer
import requests
import os

def get_model_id(model_name):
    return model_name.split('/')[-1]

def validate_model_id(model_name):
    model_id = get_model_id(model_name)
    if model_name.lower().startswith('openai/'):
        return True
    else:
        url = f"https://huggingface.co/api/models/{model_id}"
        response = requests.head(url)
        if response.status_code == 200:
            return True
        else:
            print(f"Model ID '{model_id}' validation failed with status code {response.status_code}")
            return False

def load_model(model_name):
    model_id = model_name
    try:        
        if model_name.lower().startswith('openai/'):
            model_id = get_model_id(model_name)
            print('OpenAI model: ', model_id)
            openai_api_key = os.getenv('OPENAI_API_KEY')
            if not openai_api_key:
                raise ValueError("OpenAI API key not found in environment variables.")
            #return ChatOpenAI(model=model_id, temperature=0.2, api_key=openai_api_key)
            return ChatOpenAI(model=model_id)
        else:
            huggingface_api_key = os.getenv('HUGGINGFACE_API_KEY')
            #print(f"Hugging Face API key:, ', {huggingface_api_key}")
            if not huggingface_api_key:
                raise ValueError("HuggingFace API key not found in environment variables.")
            #if not validate_model_id(model_name):
            #    raise ValueError(f"Hugging Face model ID '{model_id}' is invalid or inaccessible.")
            login(huggingface_api_key)
            print('HuggingFace model: ', model_id)
            tokenizer = AutoTokenizer.from_pretrained(model_id)
            model = AutoModelForCausalLM.from_pretrained(model_id)
            return model, tokenizer
    except Exception as e:
        print(f"Error loading model '{model_name}': {e}")
        return None, None