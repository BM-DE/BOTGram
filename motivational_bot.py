import random
import requests
import os
from datetime import datetime
import pytz

# Configuración desde variables de entorno
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

# Mensajes por categoría y área (simplificado para prueba)
mensajes = {
    "Mañana Temprano (7-9 AM)": ["Mensaje de prueba 1", "Mensaje de prueba 2", "Mensaje de prueba 3"],
    "Media Mañana (9-11 AM)": ["Mensaje de prueba 4", "Mensaje de prueba 5", "Mensaje de prueba 6"],
    "Mediodía (11 AM-1 PM)": ["Mensaje de prueba 7", "Mensaje de prueba 8", "Mensaje de prueba 9"],
    "Tarde (1-5 PM)": ["Mensaje de prueba 10", "Mensaje de prueba 11", "Mensaje de prueba 12"],
    "Noche Temprana (5-7 PM)": ["Mensaje de prueba 13", "Mensaje de prueba 14", "Mensaje de prueba 15"],
    "Noche (7-9 PM)": ["Mensaje de prueba 16", "Mensaje de prueba 17", "Mensaje de prueba 18"],
    "Noche Tardía (9-10 PM)": ["Mensaje de prueba 19", "Mensaje de prueba 20", "Mensaje de prueba 21"]
}

def enviar_mensaje_telegram(mensaje):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": mensaje}
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print(f"Respuesta de Telegram: {response.text}")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al enviar: {e}")
        return None

def seleccionar_mensajes():
    lima_tz = pytz.timezone('America/Lima')
    hora_actual = datetime.now(lima_tz).hour
    print(f"Hora detectada en Lima: {hora_actual}:00 (UTC-5)")

    if 7 <= hora_actual < 9:
        return ["Mañana Temprano (7-9 AM)"] * 3
    elif 9 <= hora_actual < 11:
        return ["Media Mañana (9-11 AM)"] * 3
    elif 11 <= hora_actual < 13:
        return ["Mediodía (11 AM-1 PM)"] * 3
    elif 13 <= hora_actual < 17:
        return ["Tarde (1-5 PM)"] * 3
    elif 17 <= hora_actual < 19:
        return ["Noche Temprana (5-7 PM)"] * 3
    elif 19 <= hora_actual < 21:
        return ["Noche (7-9 PM)"] * 3
    elif 21 <= hora_actual < 22:
        return ["Noche Tardía (9-10 PM)"] * 3
    else:
        print(f"Hora fuera de rango ({hora_actual}:00), enviando mensaje de prueba.")
        return ["Mañana Temprano (7-9 AM)"] * 3  # Mensaje de prueba fuera de rango

def main():
    print(f"Token: {BOT_TOKEN[:4]}... (ocultado), Chat ID: {CHAT_ID}")
    if not BOT_TOKEN or not CHAT_ID:
        print("Error: Faltan BOT_TOKEN o CHAT_ID")
        return
    categorias = seleccionar_mensajes()
    print(f"Categorías seleccionadas: {categorias}")
    for categoria in categorias:
        mensaje = random.choice(mensajes[categoria])
        print(f"Generando mensaje: {mensaje}")
        resultado = enviar_mensaje_telegram(mensaje)
        if resultado and resultado.get('ok'):
            print("Mensaje enviado con éxito")
        else:
            print("Fallo al enviar mensaje")

if __name__ == "__main__":
    main()
