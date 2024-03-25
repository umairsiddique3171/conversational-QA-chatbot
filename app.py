# importing dependencies
from dotenv import load_dotenv
load_dotenv() # loading .env variable as environment variables in current session

import os 
import streamlit as st
import google.generativeai as genai
from utils import set_background

# configuration with api_key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# func to load GeminiPro and get response
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])
def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response

# initial streamlit app
st.set_page_config(page_title="Q&A Chatbot")
st.header("Q&A Chatbot")

# set background
set_background('background_img.jpg')

# initialize session state for chat history if doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("#### Ask the question:",key="input")
submit = st.button("Submit")

if submit and input: 
    response= get_gemini_response(input)
    ## add user query and response to session chat history
    st.session_state['chat_history'].append(("You:",input))
    st.subheader("Response:")
    for chunk in response:
        st.write(chunk.text)
    st.session_state['chat_history'].append(("Bot:",response.text))

with st.expander('Chat History'): 
    for role,text in st.session_state['chat_history']:
        st.write(f"#### {role}")
        st.write(f"{text}")
        


                                            