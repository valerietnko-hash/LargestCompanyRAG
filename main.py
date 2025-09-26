from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model=OllamaLLM(model="llama3.2")
template="""
    You are an expert in answering questions about the 100 largest companies in the US

    Here are some relevant information about the companies:{info}

    Here is a question about the companies: {question}
"""

prompt=ChatPromptTemplate.from_template(template)
chain=prompt | model

result=chain.invoke({"info":[],"question":"Which company has the highest revenue?"})
print(result)