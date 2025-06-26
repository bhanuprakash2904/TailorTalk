# frontend/app.py

import streamlit as st
from agent import run_agent_logic  # Directly use the function instead of calling backend

st.title("📅 TailorTalk AI — Appointment Bot")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Ask to book a meeting...")

if user_input:
    st.session_state.messages.append(("user", user_input))
    
    try:
        reply = run_agent_logic(user_input)
    except Exception as e:
        reply = f"❌ Error running agent: {e}"
    
    st.session_state.messages.append(("bot", reply))

for sender, msg in st.session_state.messages:
    with st.chat_message(sender):
        st.markdown(msg)

