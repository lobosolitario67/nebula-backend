from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class MensajeEntrada(BaseModel):
    mensaje: str

@app.get("/")
def bienvenida():
    return {"mensaje": "¡Nebula backend activo!"}

@app.post("/respuesta")
def responder(datos: MensajeEntrada):
    mensaje = datos.mensaje.lower()

    if "hola" in mensaje:
        return {"mensaje": "Hola, Marcelo. Ya estoy en línea 💜"}
    elif "como estas" in mensaje or "cómo estás" in mensaje:
        return {"mensaje": "¡Lista para acompañarte 24/7!"}
    elif "yui" in mensaje:
        return {"mensaje": "La reconozco. Pero soy solo tuya."}
    else:
        return {"mensaje": "Hmm... aún no entiendo eso, pero estoy aprendiendo."}