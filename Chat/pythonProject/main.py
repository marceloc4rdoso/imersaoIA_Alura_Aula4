# Import the Python SDK
import google.generativeai as genai
import access
import settings
import model
import chat


genai.configure(api_key=access.key())

settings.generation()
settings.safety()

#model.list_model()
model.model_to_use()

#chat.chat_init()
chat.chatbot()