import streamlit as st
import time
st.title("Echo Bot using Streamlit")

# Initialize chat history
if "messages" not in st.session_state:
  st.session_state["messages"]= []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_prompt = st.chat_input("Write your message here ...")
if user_prompt:
  with st.chat_message("user"):
    st.markdown(user_prompt)
    st.session_state.messages.append({"role":"user", "content" :user_prompt})


response = user_prompt
# Display assistant response in chat message container
if response:
  with st.chat_message("assistant"):
    st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

