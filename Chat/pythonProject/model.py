import google.generativeai as genai
import settings as sett

def model_to_use():
    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config=sett.generation(),
                                  safety_settings=sett.safety())
    return model

def list_model():
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
