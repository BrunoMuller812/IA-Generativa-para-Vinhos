# Projeto de IA com Ollama para Recomendação de Vinhos 🍷🧠

Este projeto utiliza inteligência artificial generativa com o modelo **LLaMA 3.2**, através da biblioteca [LangChain](https://www.langchain.com/), para responder perguntas relacionadas a vinhos com base em uma base de dados de rótulos altamente avaliados. A aplicação pode ser executada tanto no terminal quanto por uma interface web utilizando [Streamlit](https://streamlit.io/).

---

## 🧠 Tecnologias utilizadas
- Python 🐍
- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.com/) (LLaMA 3.2)
- Streamlit
- ChromaDB com `langchain_chroma` para armazenamento vetorial

---

## ✨ Como rodar o projeto

### Pré-requisitos:

1. **Instalar o Ollama localmente**
   - Acesse: https://ollama.com/download e baixe o instalador para o seu sistema operacional.

2. **Instalar o Python e bibliotecas necessárias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Instalar o C++ Build Tools (necessário para `langchain_chroma`)**
   - Vá até: https://visualstudio.microsoft.com/visual-cpp-build-tools/
   - Durante a instalação, **selecione a opção `Desenvolvimento para Desktop com C++`**
   - Isso é necessário para que o `chromadb` funcione corretamente.

4. **Baixar os modelos necessários no Ollama**
   ```bash
   ollama pull llama3.2
   ollama pull mxbai-embed-large
   ```

---

## 🚀 Modos de execução

### 1. Rodar pelo terminal:
```bash
python main.py
```
- Interaja diretamente com o agente no terminal.

### 2. Rodar com Streamlit:
```bash
streamlit run app.py
```
- Interface web amigável para perguntas e respostas sobre vinhos 🍷

---

## 📂 Estrutura dos arquivos principais
- `main.py` → versão para terminal
- `app.py` → versão web com Streamlit
- `vector.py` → carrega a base de dados de vinhos e cria o banco vetorial
- `top_rated_wines.csv` → base de dados com os melhores vinhos avaliados

---
