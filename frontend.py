import streamlit as st
from backend import chatbot
    
thread_id = 4
CONFIG = {'configurable': {'thread_id': thread_id}}

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.write(message['content'])

with st.chat_message("assistant"):
    st.write("Hello, how are you?")

user_input = st.chat_input("Type Here")

if user_input:
    st.session_state['messages'][-1].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)
        
    st.session_state['messages'].append({"role": "user", "content": user_input})
    with st.chat_message("assistant"):
        # response = chatbot.invoke({"messages": user_input}, config= CONFIG)
        # st.text(response['messages'][-1].content)
        st.text(user_input)
        
        