# frontend/app.py

import streamlit as st
import requests

st.title("📅 TailorTalk AI — Appointment Bot")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Ask to book a meeting...")

if user_input:
    st.session_state.messages.append(("user", user_input))
    
    try:
        res = requests.post("http://localhost:8000/chat", json={"message": user_input})
        reply = res.json()["reply"]
    except Exception as e:
        reply = f"❌ Error contacting backend: {e}"
    
    st.session_state.messages.append(("bot", reply))

for sender, msg in st.session_state.messages:
    with st.chat_message(sender):
        st.markdown(msg)
