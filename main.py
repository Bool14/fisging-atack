from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
import httpx

app = FastAPI()

MAKE_WEBHOOK_URL = "https://hook.us2.make.com/g4uxj3p1ic3o4as6f1jx3sqyrxivva5l"
REDIRECT_URL = "https://www.python.org/" 

@app.get("/click")
async def handle_click(request: Request):
    email = request.query_params.get("email")
    
    if email:
        # 1. Enviar info al webhook de Make
        async with httpx.AsyncClient() as client:
            await client.post(MAKE_WEBHOOK_URL, json={"email": email}, timeout=20.0)
    
    # 2. Redirigir al usuario
    return RedirectResponse(REDIRECT_URL)
