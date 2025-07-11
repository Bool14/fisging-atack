from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import RedirectResponse
import httpx

app = FastAPI()

MAKE_WEBHOOK_URL = "https://hook.us2.make.com/g4uxj3p1ic3o4as6f1jx3sqyrxivva5l"
REDIRECT_URL = "https://sites.google.com/grande-studios.com/phishingsim/p%C3%A1gina-principal" 

@app.get("/click")
async def handle_click(request: Request, background_tasks: BackgroundTasks):
    email = request.query_params.get("email")
    
    if email:
        # Llama al webhook en background para no bloquear
        background_tasks.add_task(post_to_webhook, email)

    return RedirectResponse(REDIRECT_URL)

async def post_to_webhook(email: str):
    try:
        async with httpx.AsyncClient() as client:
            await client.post(MAKE_WEBHOOK_URL, json={"email": email}, timeout=10.0)
    except Exception as e:
        print("Error enviando a Make:", e)
