import os
from glob import glob


import google.generativeai as genai




api_key = "AIzaSyBDz5wgPJo5110mJ-GioWePswHW47GYjcA"

genai.configure(api_key=api_key)


import google.generativeai as genai

def base_model_chatbot(messages):


    # Initialize the Generative AI model
    model = genai.GenerativeModel('gemini-1.5-flash')

    # System message to set the chatbot's role
    system_message = [
        {"role": "system", "content": "You are a helpful AI chatbot that answers questions asked by the User."}
    ]
    
    # Combine the system message with user messages
    messages = system_message + messages

    # Generate content based on the messages
    conversation = " ".join([f"{msg['role']}: {msg['content']}" for msg in messages])
    response = model.generate_content(conversation)
    
    # Return the generated content
    return response.text




