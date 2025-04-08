# Importa o gerador de embeddings do Ollama
from langchain_ollama import OllamaEmbeddings

# Importa o gerenciador de banco vetorial Chroma
from langchain_chroma import Chroma

# Importa a classe Document para criar documentos estruturados
from langchain_core.documents import Document

# Importa bibliotecas padrão
import os
import pandas as pd

# Lê o arquivo CSV contendo os vinhos avaliados
df = pd.read_csv("top_rated_wines.csv")

# Remove entradas onde o tipo de uva (variety) está ausente
df = df[df['variety'].notna()]

# Cria a função de embedding usando o modelo "mxbai-embed-large" do Ollama
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# Define o diretório onde o banco vetorial será salvo
db_location = "./chrome_langchain_db"

# Verifica se o banco vetorial já existe para saber se deve adicionar documentos
add_documents = not os.path.exists(db_location)

# Se o banco vetorial ainda não existe, preparamos os documentos para adicionar
if add_documents:
    documents = []
    ids = []

    # Percorre cada linha do dataframe para transformar em um Document
    for i, row in df.iterrows():
        document = Document(
            page_content=row['name'] + " " + row['notes'],  # Conteúdo principal do documento
            metadata={  # Metadados úteis para filtragem ou explicação da resposta
                "rating": row['rating'],
                "variety": row['variety'],
                "region": row['region']
            },
            id=str(i)  # ID único para o documento
        )
        ids.append(str(i))
        documents.append(document)

# Inicializa o banco vetorial com os embeddings configurados
vector_store = Chroma(
    collection_name="top_rated_wines",  # Nome da coleção dentro do Chroma
    persist_directory=db_location,      # Diretório onde os dados serão salvos
    embedding_function=embeddings       # Função usada para gerar embeddings
)

# Se necessário, adiciona os documentos recém-criados ao banco vetorial
if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)

# Cria o retriever para buscar os documentos mais relevantes baseado em uma consulta
retriever = vector_store.as_retriever(
    search_kwargs={"k": 1}  # Define que será retornado apenas o documento mais relevante
)
