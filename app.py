import streamlit as st
import random

st.title("🤖 Free AI Chatbot")
st.write("Type a message below and chat with the bot!")

# Simple rule-based responses
responses = [
    "That's interesting! Tell me more.",
    "I see. How do you feel about that?",
    "Can you explain a bit further?",
    "Hmm, that's something to think about.",
    "Got it! What else is on your mind?"
]

user_input = st.text_input("You: ")

if user_input:
    bot_reply = random.choice(responses)
    st.write("Bot:", bot_reply)