import google.generativeai as genai
from google.colab import userdata
def key():

    api_key = userdata.get('SECRET_KEY')
    GOOGLE_API_KEY = genai.configure(api_key=api_key)
    return GOOGLE_API_KEY
