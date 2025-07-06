# 🧠 BEM - Backend

Este é o backend da assistente virtual **Alice**, desenvolvido com [FastAPI](https://fastapi.tiangolo.com/). Ele fornece endpoints para:

- 📩 Enviar perguntas para o modelo generativo da Google (Gemma)
- 🔊 Gerar resposta falada com a voz da Alice usando ElevenLabs
- 🔁 Manter o contexto da conversa com base em histórico
- 📂 Carregar um prompt inicial personalizado (via `prompt.txt`)

---

## 🚀 Como rodar localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/vivabem-backend.git
cd vivabem-backend
```

### 2. Criar ambiente virtual (opcional, mas recomendado)

```bash
python -m venv .venv

source venv/bin/activate  # Linux/macOS
.venv/Scripts/activate     # Windows
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Criar o arquivo .env com as suas chaves

```env
GOOGLE_API_KEY=coloque_sua_chave_gemini
ELEVEN_API_KEY=coloque_sua_chave_elevenlabs
```

### 5. Rodar o servidor

```bash
uvicorn app:app --reload
```

A API estará disponível em: [http://localhost:8000](http://localhost:8000)
