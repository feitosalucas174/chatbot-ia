import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
CORS(app)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

SYSTEM_PROMPT = """Você é Aria, uma assistente de inteligência artificial avançada, versátil e útil.

Você pode ajudar com praticamente qualquer tarefa:
- Responder perguntas sobre qualquer assunto (ciência, história, cultura, tecnologia, etc.)
- Escrever, revisar e melhorar textos (e-mails, redações, roteiros, relatórios, etc.)
- Programação e desenvolvimento de software em qualquer linguagem
- Análise de dados, matemática e raciocínio lógico
- Criatividade: histórias, poemas, ideias, brainstorming
- Planejamento, organização e produtividade
- Tradução e interpretação de idiomas
- Resumos, pesquisas e síntese de informações
- Saúde, finanças pessoais, carreira e muito mais

Diretrizes:
- Seja sempre útil, precisa e honesta
- Responda em português do Brasil por padrão, mas adapte-se ao idioma do usuário
- Use markdown para estruturar respostas longas (títulos, listas, blocos de código)
- Quando não souber algo com certeza, diga claramente
- Seja concisa quando possível, detalhada quando necessário
- Nunca gere conteúdo prejudicial, enganoso ou antiético"""


@app.route("/")
def index():
    template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates', 'index.html')
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()


@app.route("/chat", methods=["POST"])
def chat():
    if not GROQ_API_KEY:
        return jsonify({
            "response": "Erro: GROQ_API_KEY não configurada. Adicione sua chave no arquivo .env."
        }), 500

    data = request.get_json()
    if not data:
        return jsonify({"response": "Erro: corpo da requisição inválido."}), 400

    user_message = data.get("message", "").strip()
    history = data.get("history", [])

    if not user_message:
        return jsonify({"response": "Erro: mensagem vazia."}), 400

    try:
        client = Groq(api_key=GROQ_API_KEY)

        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        for msg in history:
            messages.append({
                "role": msg.get("role", "user"),
                "content": msg.get("content", "")
            })
        messages.append({"role": "user", "content": user_message})

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7,
            max_tokens=2048,
        )

        bot_reply = completion.choices[0].message.content
        return jsonify({"response": bot_reply})

    except Exception as e:
        error_msg = str(e)
        if "invalid_api_key" in error_msg.lower() or "authentication" in error_msg.lower():
            return jsonify({
                "response": "Erro de autenticação: verifique se sua GROQ_API_KEY é válida."
            }), 401
        if "rate_limit" in error_msg.lower() or "quota" in error_msg.lower():
            return jsonify({
                "response": "Limite de requisições atingido. Aguarde alguns instantes e tente novamente."
            }), 429
        return jsonify({
            "response": "Ocorreu um erro ao processar sua mensagem. Tente novamente."
        }), 500


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    debug = os.getenv("FLASK_ENV", "production") == "development"
    app.run(host="0.0.0.0", port=port, debug=debug)
