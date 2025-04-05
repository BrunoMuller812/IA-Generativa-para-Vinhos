# Wine Expert AI Sommelier

Este é um projeto de IA que simula um **especialista em vinhos**, utilizando modelos da **Ollama** integrados com a biblioteca **LangChain** para responder perguntas com base em dados reais de vinhos avaliados.

## Descrição

A aplicação consiste em um chatbot interativo, capaz de responder perguntas específicas sobre vinhos utilizando informações previamente vetorizadas de um dataset (`top_rated_wines.csv`). As respostas são geradas a partir de um modelo de linguagem baseado no **LLaMA 3.2**, com embeddings de alta performance (`mxbai-embed-large`) para busca semântica.

## Funcionalidades

- Responde perguntas como um sommelier virtual
- Busca informações relevantes usando embeddings vetoriais
- Utiliza prompt chaining para criar respostas contextualizadas
- Atualiza o banco vetorial automaticamente na primeira execução

## Tecnologias Utilizadas

- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.com/)
- [ChromaDB](https://www.trychroma.com/)
- Python (pandas, os)

---

## Requisitos

### 1. Python 3.10 ou superior

### 2. Instalar o [Ollama](https://ollama.com/download)

- Baixe e instale o Ollama para seu sistema operacional.
- Após instalar, execute no terminal:
  ```bash
  ollama serve
  ```
- Em seguida, baixe o modelo necessário:
  ```bash
  ollama run llama3:instruct
  ```

> **Dica:** Certifique-se de que o nome do modelo no seu código (`llama3.2`) seja o mesmo do modelo que você baixou com o Ollama.

---

### 3. Instalar as ferramentas de compilação C++

#### Windows
- Baixe e instale o [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
- Marque as opções:
  - **C++ Build Tools**
  - **Windows 10 SDK**
  - **CMake tools for Windows** (opcional, mas recomendado)

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install build-essential
```

#### macOS
- Xcode Command Line Tools:
```bash
xcode-select --install
```

---

## Como rodar o projeto

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Inicie o Ollama:
```bash
ollama serve
```

3. Execute o script principal:
```bash
python main.py
```

---

## Uso

Digite suas perguntas no terminal (exemplo):
```
Insira sua pergunta: Quais são os melhores vinhos tintos da região da Toscana?
```

Para sair do programa, digite:
```
q
```

---

## Licença

Este projeto está sob a licença MIT.
"""

# Salvar o conteúdo em um arquivo README.md
readme_path = "/mnt/data/README.md"
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

readme_path