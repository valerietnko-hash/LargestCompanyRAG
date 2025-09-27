import streamlit as st
from main import chain
from vector import retriever
import time

# Title of the app
st.title("✨ Enquiry on the 100 Largest Companies in the US")

# Retain previous inputs 
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if prompt := st.chat_input("Ask a question about the 100 largest companies in the US"):
    
    # Display user message in chat message container
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display the latest user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get the response from the model
    info = retriever.invoke(prompt)
    result=chain.invoke({"info":info,"question":prompt})

    # Simulate streaming by displaying the answer character by character
    assistant_placeholder = st.empty()
    streamed_text = ""
    for char in result:
        streamed_text += char
        assistant_placeholder.markdown(streamed_text)
        time.sleep(0.02)  # Small delay for effect



    # Display assistant response in chat message container
    st.session_state.messages.append({"role": "assistant", "content": result})
    #st.chat_message("assistant").markdown(result)
    assistant_placeholder.markdown(result)