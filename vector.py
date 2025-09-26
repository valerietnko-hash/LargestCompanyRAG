from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df=pd.read_csv("largest_company.csv")
embeddings=OllamaEmbeddings(model="mxbai-embed-large")

db_location="./chroma_langchain_db"
add_documents=not os.path.exists(db_location)

if add_documents:
    documents=[]
    ids=[]

    for i,row in df.iterrows():
        document=Document(
            # querying
            page_content=row["Name"]+" "+row["Headquarters"],
            metadata={"industry":row["Industry"],"rank":row["Rank"],"revenue":row["Revenue (USD millions)"],"revenue growth":row["Revenue growth"],"employees":row["Employees"]},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)

vectorstore=Chroma(
    collection_name="largest_company",
    embedding_function=embeddings,
    persist_directory=db_location# store permanently
)

if add_documents:
    vectorstore.add_documents(documents,ids=ids)

# Search
retriever=vectorstore.as_retriever(
    search_kwargs={"k":1}
    )