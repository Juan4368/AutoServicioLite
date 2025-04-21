from fastapi import FastAPI
from dotenv import load_dotenv
import os
from config import get_db
import uvicorn
import webbrowser
import threading
import time
from fastapi.middleware.cors import CORSMiddleware
from app.routes import productos_router  # importa tu router

app = FastAPI(
    title="POS API",
    version="1.0.0",
    description="API para gestión de productos con arquitectura limpia",
    root_path="/AutoServicioLite",
    docs_url="/docs",  # Accesible desde /AutoServicioLite/docs
    redoc_url=None,
    openapi_url="/openapi.json"
)

# Middleware opcional para CORS (útil si tienes frontend separado)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en producción: ["https://tu-frontend.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"mensaje": "API POS en ejecución 🚀"}

def open_chrome():
    time.sleep(1)  # Espera a que el server arranque

    url = "http://127.0.0.1:8000/docs"

    # Intenta usar específicamente Google Chrome
    chrome_paths = [
        "C://Program Files//Google//Chrome//Application//chrome.exe",
        "C://Program Files (x86)//Google//Chrome//Application//chrome.exe",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/usr/bin/google-chrome",
        "/usr/bin/chromium-browser"
    ]

    for path in chrome_paths:
        if os.path.exists(path):
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(path))
            webbrowser.get('chrome').open_new(url)
            return

    # Si no encuentra Chrome, abre con el navegador por defecto
    webbrowser.open_new(url)

if __name__ == "__main__":
    threading.Thread(target=open_chrome).start()
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

# Cargar el archivo correspondiente al entorno
env = os.getenv("APP_ENV", "dev")
load_dotenv(dotenv_path=f".env")

""" settings = get_db()
app = FastAPI(title=settings.app_name, debug=settings.debug)
 """
""" @app.get("/")
def read_root():
    return {
        "app": settings.app_name,
        "debug": settings.debug,
        "env": settings.environment,
    } """

# Incluir rutas
app.include_router(productos_router.router)
