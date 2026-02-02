import streamlit as st
from transformers import pipeline, Conversation

# Load a pre-trained conversational model
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

st.title("🤖 Free AI Chatbot")
st.write("Type a message below and chat with the bot!")

# Keep track of conversation across turns
if "conversation" not in st.session_state:
    st.session_state.conversation = None

user_input = st.text_input("You: ")

if user_input:
    if st.session_state.conversation is None:
        st.session_state.conversation = Conversation(user_input)
    else:
        st.session_state.conversation.add_user_input(user_input)

    response = chatbot(st.session_state.conversation)
    st.write("Bot:", response.generated_responses[-1])