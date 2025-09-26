import streamlit as st

# Title of the app
st.title("RAG with the 100 Largest Companies in the US")

# Retain previous inputs 
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])