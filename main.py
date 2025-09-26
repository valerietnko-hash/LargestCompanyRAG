from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model=OllamaLLM(model="llama3.2")
template="""
    You are an expert in answering questions about the 100 largest companies in the US

    Here are some relevant information about the companies:{info}

    Here is a question about the companies: {question}
"""

prompt=ChatPromptTemplate.from_template(template)
chain=prompt | model

while True:
    print("\n\n----------------------")
    question=input("Enter your question (q to quit): ")
    print("\n\n")
    if question=="q":
        break
    info=retriever.invoke(question)
    result=chain.invoke({"info":info,"question":question})
    print(result)