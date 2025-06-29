import random
import requests
import os
from datetime import datetime
import pytz

# Configuración desde variables de entorno
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

# Mensajes motivacionales
mensajes_por_categoria = {
    "8:00": [
        "¡Buenos días! El mundo te espera. Explora un nuevo lugar en Lima hoy.",
        "¡Despierta tu social! Da un pequeño paso para conectar con alguien."
    ],
    "10:00": [
        "Tu voz importa. ¡Practica una conversación hoy!",
        "La confianza crece con la acción. ¡Intenta algo nuevo!"
    ],
    "12:45": [
        "¡Hora de inspirarte! Cada paso te acerca a tus sueños.",
        "¡Sigue adelante! Tus habilidades sociales se fortalecen."
    ]
}

def enviar_mensaje_telegram(mensaje):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": mensaje}
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print(f"Respuesta: {response.text}")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def seleccionar_mensaje():
    lima_tz = pytz.timezone('America/Lima')
    hora_actual = datetime.now(lima_tz).hour
    print(f"Hora en Lima: {hora_actual}:00")

    if hora_actual == 8:
        return random.choice(mensajes_por_categoria["8:00"])
    elif hora_actual == 10:
        return random.choice(mensajes_por_categoria["10:00"])
    elif hora_actual == 12:
        return random.choice(mensajes_por_categoria["12:45"])
    else:
        return random.choice(mensajes_por_categoria["12:45"])  # Default para pruebas

def main():
    if not BOT_TOKEN or not CHAT_ID:
        print("Error: Faltan token o chat ID")
        return
    mensaje = seleccionar_mensaje()
    print(f"Mensaje: {mensaje}")
    resultado = enviar_mensaje_telegram(mensaje)
    if resultado and resultado.get('ok'):
        print("Mensaje enviado con éxito")
    else:
        print("Fallo al enviar mensaje")

if __name__ == "__main__":
    main()