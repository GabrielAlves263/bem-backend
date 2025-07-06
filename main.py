import google.generativeai as genai
import speech_recognition as sr
from elevenlabs import play
from elevenlabs.client import ElevenLabs

genai.configure(api_key="AIzaSyB5qRu7RPEaj6gSNiuagVvX28VkN-eX9DI")
elevenlabs = ElevenLabs(
    api_key="sk_d2c0ca5df7924c1cb2dbe95cfb629f03742ee57c91b24e15",
)

modelo = genai.GenerativeModel("gemma-3n-e2b-it")


def carregar_prompt(caminho="prompt.txt"):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return arquivo.read()


prompt = carregar_prompt()

chat = modelo.start_chat(
    history=[
        {
            "role": "user",
            "parts": [prompt],
        },
    ]
)


def ouvir_microfone():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as fonte:
        print("🎤 Fale algo...")
        reconhecedor.adjust_for_ambient_noise(fonte)
        audio = reconhecedor.listen(fonte)

        try:
            texto = reconhecedor.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {texto}")
            return texto
        except sr.UnknownValueError:
            print("Não entendi.")
            return None
        except sr.RequestError:
            print("Erro ao se conectar ao Google Speech.")
            return None


def enviar_para_ia(pergunta):
    resposta = chat.send_message(pergunta)
    return resposta.text


def falar_resposta(texto):
    audio = elevenlabs.text_to_speech.convert(
        text=texto,
        voice_id="SAz9YHcvj6GT2YYXdXww",
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128",
    )
    play(audio)


while True:
    pergunta = ouvir_microfone()
    if pergunta:
        resposta = enviar_para_ia(pergunta)
        print(f"IA: {resposta}")
        # falar_resposta(resposta)
