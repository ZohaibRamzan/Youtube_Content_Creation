import streamlit as st

st.title("Chat elements from Streamlit")
prompt=st.chat_input("Say Something ...")

if prompt:
    st.write(f"Message by user: {prompt}")

with st.chat_message(name="assistant"):
    st.markdown("Hey I am your AI based Assistant")