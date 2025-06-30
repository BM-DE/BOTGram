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
        "Hoy es el día en que conoces a esa chica tímida que ha estado esperando a alguien como tú. Sal y muestra tu confianza, ella estará encantada de conocerte.",
        "Imagina la mirada de esa niña bonita y sumisa cuando te acerques a ella con seguridad. Hoy es el día en que haces realidad sus sueños y los tuyos.",
        "Cada tímida que conoces es una oportunidad para crear una conexión única. Sal y demuéstrales que eres el hombre que siempre han deseado.",
        "Hoy es el día perfecto para encontrar a esa chica que te espera con ansias. Sal y haz que tu presencia sea inolvidable.",
        "Las chicas tímidas solo necesitan a alguien que las haga sentir seguras. Sé ese alguien hoy y cambia su vida para siempre."
    ],
    "10:00": [
        "Imagina el placer de estar con una nalgona y bonita. Hoy es el día en que haces realidad esa fantasía. No dudes de ti mismo, mereces estar con alguien así.",
        "Las culonas aprecian la confianza y la seguridad. Sé ese hombre hoy y conquista sus corazones. No te sientas poco hombre, tú eres más que suficiente para ellas.",
        "Hoy es el día perfecto para encontrar a esa culona que te ha estado esperando. Sal y haz que tu encuentro sea inolvidable. Tu valía no está en duda.",
        "Las mujeres con nalgas grandes son un sueño hecho realidad. Sal y enamóralas con tu presencia y confianza. No te sientas inferior, tú eres justo lo que ellas necesitan.",
        "Las culonas y tetonas saben lo que quieren y tú eres justo lo que ellas desean. Sal y demuéstrales que eres el hombre ideal. No te sientas inferior, tú eres más que capaz de satisfacerlas."
    ],
    "12:45": [
        "Hazlo por esas niñas sumisas/tímidas de caras bonitas.",
        "Hoy tienes que sacarle al número a esa potona, tú puedes, recuérdalo.",
        "Pensar en cómo una niña sumisa te obedecería y te seguiría sin dudar debería motivarte a salir y encontrar a la pareja perfecta. Tú eres su sueño hecho realidad.",
        "Visualiza a una niña sumisa cumpliendo todos tus deseos, adorándote y siguiendo tus órdenes. Esa podría ser tu realidad si sales y te arriesgas a encontrar a la mujer perfecta para ti.",
        "Imagina la satisfacción de dominar a puras niñas bonitas de lentes, de ver cómo te admiran y te desean. Sal y encuentra a esa chica que está esperando a alguien como tú para guiarla y protegerla."
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
