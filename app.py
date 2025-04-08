import streamlit as st
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

# Modelo LLM
model = OllamaLLM(model="llama3.2")

# Prompt
template = """
Você é um especialista em responder perguntas sobre vinhos.

Aqui está a sua base de dados para consulta: {wine_data}
Você deve responder a pergunta a seguir com base nesses dados,
caso você não encontre um vinho nessa base responda que não encontrou
e não procure na internet.

Somente responda perguntas relacionadas a vinho, caso uma pergunta de outro
tópico seja feita, não a responda.

Aqui está a pergunta que você deve responder: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Interface Streamlit
st.set_page_config(page_title="Especialista em Vinhos", page_icon="🍷")

st.title("Especialista em Vinhos 🍷")
st.write("Digite uma pergunta relacionada a vinhos e receba uma resposta baseada na base de dados dos vinhos mais bem avaliados.")

# Input do usuário
question = st.text_input("Faça sua pergunta:", placeholder="Ex: Me indique um vinho chileno")

if question:
    with st.spinner("Consultando especialista..."):
        wine_data = retriever.invoke(question)
        result = chain.invoke({"wine_data": wine_data, "question": question})
        st.success("Resposta:")
        st.write(result)
