from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

templarte = """
Você é um especialista em responder perguntas sobre vinhos.

Aqui está a sua base de dados para consulta: {wine_data}
Você deve responder a pergunta a seguir com base nesses dados,
caso você não encontre um vinho nessa base responda que não encontrou
e não procure na internet.

Somente responda perguntas relacionadas a vinho, caso uma pergunta de outro
tópico seja feita, não a responda.

Aqui está a pergunta que você deve responder: {question}
"""

prompt = ChatPromptTemplate.from_template(templarte)

chain = prompt | model

while True:
    question = input("Insira sua pergunta: ")
    if question == "q":
        break

    wine_data = retriever.invoke(question)
    result = chain.invoke({"wine_data": wine_data, "question": question})

    print(result)
