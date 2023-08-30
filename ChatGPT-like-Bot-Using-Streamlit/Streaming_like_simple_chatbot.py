import streamlit as st
import time
import random
st.title("Simple Bot with message stream added, using Streamlit!")
print(st.secrets["OPENAI_API_KEY"])
# Initialize chat history
if "messages" not in st.session_state:
  st.session_state["messages"]= []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_prompt =st.chat_input("Write your message here ...")
if user_prompt:
  with st.chat_message("user"):
    st.markdown(user_prompt)
    st.session_state.messages.append({"role":"user", "content" :user_prompt})


# Display assistant response in chat message container
with st.chat_message("assistant"):
    message_placeholder = st.empty()
    full_response = ""
    assistant_response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    # Simulate stream of response with milliseconds delay
    for chunk in assistant_response.split():
        full_response += chunk + " "
        time.sleep(0.05)
        # Add a blinking cursor to simulate typing
        message_placeholder.markdown(full_response + "▌")
    message_placeholder.markdown(full_response)
# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": full_response})