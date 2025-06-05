import streamlit as st
from chatbot import Chatbot
import time

def close_chat():
    current_time = time.time()

    time_taken = current_time - st.session_state.time_taken
    if time_taken > 60:
        with st.chat_message("system"):
            st.markdown(f"**Chat ended due to inactivity. Time Elapsed: {int(time_taken)} seconds**")
            st.stop()

st.title("Rawry_ZA Chatbot")

with open("docs/Galaletsang_Modimola_Resume.pdf", "rb") as file:
    cv_data = file.read()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chatbot" not in st.session_state:
    st.session_state.chatbot = Chatbot()

if "time_taken" not in st.session_state:
    st.session_state.time_taken = time.time()   

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask something about Galaletsang...", on_submit=close_chat)

if prompt:

    st.session_state.time_taken = time.time()

    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        with st.spinner("Generating response..."):
            response = st.session_state.chatbot.get_response(st.session_state.messages)

    except Exception as e:
        st.error(f"Error: {e}")
        response = "Sorry, I couldn't generate a response."

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

    if "cv" in response.lower() or "resume" in response.lower():
        st.download_button(
            label="📄 Download CV",
            data=cv_data,
            file_name="your_resume_or_cv.pdf",
            mime="application/pdf"
        )

  

