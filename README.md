# chatbot-ia

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=flat&logo=flask&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Gemini-1.5%20Flash-4285F4?style=flat&logo=google&logoColor=white)
![Deploy](https://img.shields.io/badge/Deploy-Render-46E3B7?style=flat&logo=render&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

Chatbot de IA especializado em desenvolvimento de software, construído com Python/Flask e Google Gemini 1.5 Flash. Interface moderna com tema escuro/claro, histórico de conversa e suporte a Markdown com blocos de código.

![screenshot](https://via.placeholder.com/820x460/0f1117/3b82f6?text=DevBot+Screenshot)

## Funcionalidades

- Respostas geradas pelo Google Gemini 1.5 Flash
- System prompt especializado em desenvolvimento de software
- Histórico de conversa mantido entre mensagens
- Renderização de Markdown (blocos de código, negrito, itálico)
- Tema escuro/claro com persistência via localStorage
- Indicador de "digitando..." animado
- Interface responsiva para mobile
- Sugestões de perguntas na tela inicial

---

## Instalação

### Pré-requisitos

- Python 3.10 ou superior
- pip

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/chatbot-ia.git
cd chatbot-ia

# 2. Crie e ative um ambiente virtual
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure as variáveis de ambiente
cp .env.example .env
# Edite o arquivo .env e adicione sua GEMINI_API_KEY
```

---

## Como obter a API Key do Gemini

1. Acesse [Google AI Studio](https://aistudio.google.com/)
2. Faça login com sua conta Google
3. Clique em **"Get API key"** → **"Create API key"**
4. Copie a chave gerada
5. Cole no arquivo `.env`:

```
GEMINI_API_KEY=AIzaSy...sua_chave_aqui
```

> O plano gratuito do Gemini 1.5 Flash inclui 15 requisições/minuto e 1 milhão de tokens/dia — mais que suficiente para uso pessoal.

---

## Rodando localmente

```bash
# Certifique-se de que o venv está ativado e o .env configurado
python app.py
```

Acesse [http://localhost:5000](http://localhost:5000) no navegador.

Para rodar em modo desenvolvimento com hot-reload:

```bash
FLASK_ENV=development python app.py
```

---

## Deploy no Render

### 1. Suba o código para o GitHub

```bash
git add .
git commit -m "feat: projeto inicial chatbot-ia"
git push origin main
```

### 2. Crie o serviço no Render

1. Acesse [render.com](https://render.com) e faça login
2. Clique em **"New +"** → **"Web Service"**
3. Conecte seu repositório GitHub
4. Configure o serviço:

| Campo | Valor |
|-------|-------|
| **Name** | chatbot-ia |
| **Runtime** | Python 3 |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app` |
| **Instance Type** | Free |

### 3. Configure a variável de ambiente

No painel do Render, vá em **"Environment"** e adicione:

```
GEMINI_API_KEY = sua_chave_aqui
```

### 4. Deploy

Clique em **"Create Web Service"**. O Render fará o build e deploy automaticamente.

A cada `git push` para a branch `main`, o Render realiza um novo deploy.

---

## Estrutura do projeto

```
chatbot-ia/
├── app.py              # Servidor Flask + integração Gemini
├── requirements.txt    # Dependências Python
├── .env.example        # Template de variáveis de ambiente
├── .gitignore
├── README.md
└── templates/
    └── index.html      # Interface do chat (HTML + CSS + JS)
```

---

## Tecnologias

| Tecnologia | Uso |
|-----------|-----|
| [Python 3.10+](https://python.org) | Linguagem principal do backend |
| [Flask](https://flask.palletsprojects.com) | Servidor web e roteamento |
| [Flask-CORS](https://flask-cors.readthedocs.io) | Cross-Origin Resource Sharing |
| [google-generativeai](https://pypi.org/project/google-generativeai/) | SDK do Google Gemini |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Carregamento de variáveis de ambiente |
| [Gunicorn](https://gunicorn.org) | Servidor WSGI para produção |

---

## Licença

MIT — veja [LICENSE](LICENSE) para detalhes.
