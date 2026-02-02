import streamlit as st
import requests

# Hugging Face Inference API endpoint (DialoGPT-medium is free to use)
API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"

# Replace with your own Hugging Face API token (free signup at huggingface.co)
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

st.title("🤖 AI Chatbot (Hugging Face API)")
st.write("Ask me anything and I'll reply with AI-powered responses!")

user_input = st.text_input("You: ")

if user_input:
    output = query({"inputs": user_input})
    # The API returns a list of generated_text
    if isinstance(output, list) and "generated_text" in output[0]:
        st.write("Bot:", output[0]["generated_text"])
    else:
        st.write("Bot: Sorry, I couldn't generate a reply.")