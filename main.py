# Importa o modelo de linguagem da biblioteca langchain_ollama
from langchain_ollama.llms import OllamaLLM

# Importa o template de prompt para estruturar a interação com o modelo
from langchain_core.prompts import ChatPromptTemplate

# Importa o retriever (responsável por buscar dados relevantes) do arquivo vector.py
from vector import retriever

# Inicializa o modelo LLaMA 3.2 via Ollama
model = OllamaLLM(model="llama3.2")

# Define o template do prompt que será enviado ao modelo
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

# Cria um prompt formatável a partir do template
prompt = ChatPromptTemplate.from_template(templarte)

# Cria a cadeia (pipeline) unindo o prompt ao modelo de linguagem
chain = prompt | model

# Inicia um loop para interação contínua com o usuário
while True:
    # Solicita ao usuário que insira uma pergunta
    question = input("Insira sua pergunta: ")
    
    # Se o usuário digitar "q", o loop é encerrado
    if question == "q":
        break

    # Usa o retriever para buscar os dados relevantes da base de vinhos
    wine_data = retriever.invoke(question)

    # Envia os dados e a pergunta para a cadeia (modelo) e obtém a resposta
    result = chain.invoke({"wine_data": wine_data, "question": question})

    # Exibe a resposta do modelo no terminal
    print(result)