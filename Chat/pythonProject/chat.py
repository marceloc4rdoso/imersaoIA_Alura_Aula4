import model

def chat_init():
    response = model.model_to_use().generate_content("Olá! Vamos aprender conteúdo sobre IA! De de sugestões.")
    print(response.text)
def chatbot():
    chat = model.model_to_use().start_chat(history=[])
    prompt = input("Esperando o prompt: ").lower()

    while prompt != "fim":
        response = chat.send_message(prompt)
        print(f"Resposta: {response.text}")
        prompt = input("Esperando o prompt: ").lower()
    # Imprimindo o histórico
    print('-----------HISTÓRICO DESSE CHAT------------')
    for message in chat.history:
        print(f'**{message.role}**: {message.parts[0].text}')
        print('-------------------------------------------')








