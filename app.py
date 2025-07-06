import os

import google.generativeai as genai
from dotenv import load_dotenv
from elevenlabs import ElevenLabs, save
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
elevenlabs = ElevenLabs(
    api_key=os.getenv("ELEVEN_API_KEY"),
)

modelo = genai.GenerativeModel("gemma-3n-e2b-it")

app = FastAPI()


def carregar_prompt(caminho="prompt.txt"):
    with open(caminho, "r", encoding="utf-8") as f:
        return f.read()


prompt = carregar_prompt()

chat = modelo.start_chat(
    history=[
        {
            "role": "user",
            "parts": [prompt],
        },
    ]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://bem-delta.vercel.app"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Pergunta(BaseModel):
    texto: str


@app.post("/perguntar")
def perguntar(dados: Pergunta):
    resposta = chat.send_message(dados.texto)
    return {"resposta": resposta.text}


@app.post("/falar")
def falar(dados: Pergunta):
    audio = elevenlabs.text_to_speech.convert(
        text=dados.texto,
        voice_id="SAz9YHcvj6GT2YYXdXww",
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128",
    )
    caminho = "resposta.mp3"
    save(audio, caminho)
    return FileResponse(caminho, media_type="audio/mpeg")
