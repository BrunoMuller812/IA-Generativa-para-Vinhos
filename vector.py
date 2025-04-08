from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_csv("top_rated_wines.csv")
df = df[df['variety'].notna()]
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chrome_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []

    for i, row in df.iterrows():
        document = Document(
            page_content=row['name'] + " " + row['notes'],
            metadata={"rating" : row['rating'], "variety" : row['variety'],"region" : row['region']},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)

vector_store = Chroma(
    collection_name="top_rated_wines",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    vector_store.add_documents(documents= documents, ids=ids)

retriever =  vector_store.as_retriever(
    search_kwargs={"k": 1}
)