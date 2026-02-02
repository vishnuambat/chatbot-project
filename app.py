import streamlit as st
from transformers import pipeline

# Load a pre-trained text generation model
chatbot = pipeline("text-generation", model="gpt2")

st.title("🤖 Free AI Chatbot")
st.write("Type a message below and chat with the bot!")

user_input = st.text_input("You: ")

if user_input:
    response = chatbot(user_input, max_length=100, num_return_sequences=1)
    st.write("Bot:", response[0]['generated_text'])