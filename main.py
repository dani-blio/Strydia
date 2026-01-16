import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from coach_llm import generate_coach_reply

load_dotenv()

app = FastAPI(title="STRYDIA Backend")

allowed = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in allowed if o.strip()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/ai/coach/chat", response_model=ChatResponse)
def coach_chat(req: ChatRequest):
    context = (
        "Entrenador STRYDIA. Si el usuario indica dolor agudo, mareos, fiebre o lesión: "
        "recomienda parar y consultar profesional."
    )
    reply = generate_coach_reply(req.message, context=context)
    return ChatResponse(reply=reply)
