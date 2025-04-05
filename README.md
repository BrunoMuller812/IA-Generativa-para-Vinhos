---

Wine Expert AI Sommelier

Este é um projeto de IA que simula um especialista em vinhos, utilizando modelos da Ollama integrados com a biblioteca LangChain para responder perguntas com base em dados reais de vinhos avaliados.

Descrição

A aplicação consiste em um chatbot interativo, capaz de responder perguntas específicas sobre vinhos utilizando informações previamente vetorizadas de um dataset (top_rated_wines.csv). As respostas são geradas a partir de um modelo de linguagem baseado no LLaMA 3.2, com embeddings de alta performance (mxbai-embed-large) para busca semântica.

Funcionalidades

Responde perguntas como um sommelier virtual

Busca informações relevantes usando embeddings vetoriais

Utiliza prompt chaining para criar respostas contextualizadas

Atualiza o banco vetorial automaticamente na primeira execução


Tecnologias Utilizadas

LangChain

Ollama

ChromaDB

Python (pandas, os)



---

Requisitos

1. Python 3.10 ou superior

2. Instalar o Ollama

Baixe e instale o Ollama para seu sistema operacional.

Após instalar, execute no terminal:

ollama serve

Em seguida, baixe o modelo necessário:

ollama run llama3:instruct


> Dica: Certifique-se de que o nome do modelo no seu código (llama3.2) seja o mesmo do modelo que você baixou com o Ollama.




---

3. Instalar as ferramentas de compilação C++

Windows

Baixe e instale o Microsoft C++ Build Tools

Marque as opções:

C++ Build Tools

Windows 10 SDK

CMake tools for Windows (opcional, mas recomendado)



Linux

sudo apt update
sudo apt install build-essential

macOS

xcode-select --install


---

Executando o Projeto

1. Clone o repositório:

git clone https://github.com/seu-usuario/wine-expert-ai.git
cd wine-expert-ai


2. Instale as dependências:

pip install -r requirements.txt


3. Execute o script:

python main.py


4. Faça perguntas sobre vinhos! Para sair, digite q.




---

Exemplo de uso

Insira sua pergunta: Qual vinho combina com massas leves?


---


