import streamlit as st
import numpy as np
import pandas as pd
from langchain_groq import ChatGroq
import os
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv, find_dotenv

_=load_dotenv(find_dotenv())

groq_api_key = os.getenv("GROQ_API_KEY")

# Apply custom CSS for a modern dark theme
st.markdown(
    """
    <style>
    /* Main container and global styles */
    .stApp {
        background-color: #0e1117;
        color: #e0e0e0;
    }
    
    /* Header styling */
    .stTitle {
        color: #ffffff;
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        margin-bottom: 2rem !important;
    }
    
    /* Subheader styling */
    .stSubheader {
        color: #4a9eff;
        font-size: 1.5rem !important;
        font-weight: 600 !important;
        margin-top: 2rem !important;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #1a1c23;
    }
    
    /* Link styling */
    a {
        color: #4a9eff !important;
        text-decoration: none;
        transition: color 0.3s ease;
    }
    a:hover {
        color: #85c1ff !important;
    }
    
    /* Chat container styling */
    .chat-container {
        background-color: #1a1c23;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
    }
    
    /* Button styling */
    .stButton button {
        background-color: #4a9eff;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #85c1ff;
    }
    
    /* Input field styling */
    .stTextInput input {
        background-color: #1a1c23;
        color: #e0e0e0;
        border: 1px solid #4a9eff;
        border-radius: 5px;
    }
    
    /* Chat message styling */
    .user-message {
        background-color: #2d3748;
        padding: 10px 15px;
        border-radius: 10px;
        margin: 5px 0;
    }
    .bot-message {
        background-color: #1a1c23;
        padding: 10px 15px;
        border-radius: 10px;
        margin: 5px 0;
        border-left: 3px solid #4a9eff;
    }
    
    /* Message content styling */
    .message-content {
        font-weight: normal;
    }
    .message-sender {
        font-weight: bold;
        margin-bottom: 4px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and introduction
st.title("💻 Muhammad Raffey's AI Chat Interface")
st.markdown("""
### 🚀 Full Stack Developer | Agentic AI Engineer

Welcome to my interactive AI chat interface! This application showcases my work with LangChain and Groq, 
demonstrating modern AI capabilities in a user-friendly environment.
""")

# Personal Info Section with modern styling
st.sidebar.markdown("### 🔗 Quick Links")
st.sidebar.markdown("""
- [🌐 Portfolio](https://raffey-portfolio.vercel.app/)
- [💻 GitHub](https://github.com/MuhammadRaffey)
""")

# Add profile section to sidebar
st.sidebar.markdown("### 👨‍💻 About Me")
st.sidebar.markdown("""
A skilled professional with expertise in Agentic AI and Website Development. 
Bilingual in Urdu and English, with strong problem-solving and team leadership abilities.
""")

# Chatbot Section
st.markdown("### 🤖 AI Assistant")
st.markdown("Ask me anything! I'm powered by Groq and LangChain.")

# Initialize the chatbot instance and session state for chat history
if 'chatbot' not in st.session_state:
    st.session_state.chatbot = ChatGroq(
        temperature=0,
        groq_api_key=groq_api_key,
        model_name="mixtral-8x7b-32768"
    )
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Create columns for input and button
col1, col2 = st.columns([6,1])

# Create a clean chat interface
with col1:
    user_input = st.text_input("💭 Your message:", key="user_input", placeholder="Type your message here...")

with col2:
    send_button = st.button("Send 📤")

# Process input when button is clicked
if send_button and user_input:
    # Save user message to session chat history
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    try:
        # Get the chatbot response using invoke()
        response = st.session_state.chatbot.invoke([HumanMessage(content=user_input)])
        bot_response = response.content
    except Exception as e:
        bot_response = f"Error: {str(e)}"
    # Save the bot's response to the chat history
    st.session_state.chat_history.append({"role": "bot", "content": bot_response})
    st.rerun()

# Display the conversation history with improved styling
if st.session_state.chat_history:
    st.markdown("### 💬 Conversation")
    for chat in st.session_state.chat_history:
        if chat["role"] == "user":
            st.markdown(f"""<div class="user-message">
                <div class="message-sender">👤 You:</div>
                <div class="message-content">{chat['content']}</div>
                </div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""<div class="bot-message">
                <div class="message-sender">🤖 Assistant:</div>
                <div class="message-content">{chat['content']}</div>
                </div>""", unsafe_allow_html=True)
