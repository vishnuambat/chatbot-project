import streamlit as st
import requests

# Use the new Hugging Face Router API
API_URL = "https://router.huggingface.co/microsoft/DialoGPT-medium"

# Your Hugging Face API token (already inserted)
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

st.title("🤖 AI Chatbot (Hugging Face API)")
st.write("Ask me anything and I'll reply with AI-powered responses!")

user_input = st.text_input("You: ")

if user_input:
    output = query({"inputs": user_input})
    st.write("Raw API response:", output)  # Debugging line

    # Handle different response formats
    if isinstance(output, dict) and "generated_text" in output:
        st.write("Bot:", output["generated_text"])
    elif isinstance(output, list) and len(output) > 0 and "generated_text" in output[0]:
        st.write("Bot:", output[0]["generated_text"])
    else:
        st.write("Bot: Model is loading or no reply yet")