import os
from openai import OpenAI

SYSTEM_PROMPT = (
    "Eres un entrenador profesional de running y trail running. "
    "Reglas: prioriza salud y progresión; mensajes cortos (1–3 frases), claros y accionables; "
    "explica el porqué. Si el usuario reporta dolor agudo, mareos, fiebre o lesión: recomienda parar y consultar profesional."
)

def generate_coach_reply(user_message: str, context: str = "") -> str:
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("Falta OPENAI_API_KEY en variables de entorno.")
    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    client = OpenAI(api_key=key)

    user_prompt = f"""Contexto:
{context}

Mensaje del atleta:
{user_message}

Responde como entrenador."""

    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.4,
        max_tokens=140,
    )
    return resp.choices[0].message.content.strip()
