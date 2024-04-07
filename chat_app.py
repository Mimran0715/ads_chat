import ollama
import streamlit as st

st.title("ADS Chat")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

def res_generator():
    stream = ollama.chat(model="llama2", 
                        messages=st.session_state["messages"],
                        stream=True)
    for chunk in stream:
        yield chunk['message']['content']

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input('What is up?'):
    st.session_state["messages"].append({"role":"user", "content":prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # response = ollama.chat(model="llama2" ,
        #                        messages=st.session_state['messages'],
        #                        stream=False)
        #message = response["message"]["content"]
        message=st.write_stream(res_generator())
        #st.markdown(message)
        st.session_state["messages"].append({"role":"assistant", "content":message})