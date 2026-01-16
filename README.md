# STRYDIA Backend (FastAPI)

## Requisitos
- Python 3.11+

## Configuración
Copia `.env.example` a `.env` y rellena:
- OPENAI_API_KEY
- ALLOWED_ORIGINS (ej: http://localhost:5173)

## Ejecutar
```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

## Endpoints
- GET /health
- POST /ai/coach/chat
