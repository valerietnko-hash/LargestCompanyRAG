import streamlit as st
from main import chain
from vector import retriever

# Title of the app
st.title("RAG with the 100 Largest Companies in the US")

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
    #st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get the response from the model
    info = retriever.invoke(prompt)
    result=chain.invoke({"info":info,"question":prompt})

    # Display assistant response in chat message container
    st.session_state.messages.append({"role": "assistant", "content": result})
    st.chat_message("assistant").markdown(result)