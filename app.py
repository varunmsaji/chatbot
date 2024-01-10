from dotenv import load_dotenv
import streamlit as st 
import google.generativeai as genai 
import os
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question,stream=True)
    return response


st.set_page_config(page_title="QA bot")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []


input = st.text_input("input",key="input")

submit = st.button("ask the question")

if submit and input:
    response = get_gemini_response(input)

    st.session_state['chat_history'].append(("you",input))
    st.subheader("the response is")
    for chunk in response:
        st.write(chunk)
        st.session_state['chat_history'].append(("bot",chunk.text))

st.subheader("the chat history is")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")
