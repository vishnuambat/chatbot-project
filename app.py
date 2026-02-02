import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
headers = {"Authorization": "Bearer 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"}  # paste your token here

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

st.title("🤖 AI Chatbot (Hugging Face API)")
st.write("Ask me anything and I'll reply with AI-powered responses!")

user_input = st.text_input("You: ")

if user_input:
    output = query({"inputs": user_input})
    # Handle both dict and list formats
    if isinstance(output, dict) and "generated_text" in output:
        st.write("Bot:", output["generated_text"])
    elif isinstance(output, list) and len(output) > 0 and "generated_text" in output[0]:
        st.write("Bot:", output[0]["generated_text"])
    else:
        st.write("Bot: (Model is loading or no reply yet)")