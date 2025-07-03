import random
import requests
import os
from datetime import datetime
import pytz

# Configuración desde variables de entorno
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

# Mensajes por categoría y área (modificados según tu lista)
mensajes = {
    "Mañana Temprano (7-9 AM)": [
        "¡Buenos días! ☀️ Hoy es una nueva oportunidad para invertir en la persona más importante: TÚ. Cada pequeña elección saludable que hagas es un acto de amor propio.",
        "Tu cuerpo ha estado en ayunas toda la noche. ¡Regálale un gran vaso de agua para despertar tus órganos y empezar el día con energía! 💧",
        "No es solo comida, es combustible. Elige un desayuno que te nutra y te prepare para conquistar el día. 🍓🥑"
    ],
    "Media Mañana (9-11 AM)": [
        "¡Esa sonrisa es poderosa! Un buen cepillado por la mañana no solo protege tus dientes, sino que te da frescura y confianza.",
        "¡Buenos días, piel! Una limpieza e hidratación rápidas la preparan y protegen de todo el día. ¡Es tu escudo de belleza! 🧴",
        "El sol es vida, pero tu piel necesita protección. ¿Reaplicaste tu protector solar? Es el mejor hábito antiedad que puedes tener. ☀️"
    ],
    "Mediodía (11 AM-1 PM)": [
        "Alto ahí! Es momento de una pausa para beber agua. Tu piel, tu cerebro y tus músculos te lo agradecerán enormemente. 💧",
        "¿Sientes un poco de hambre? Elige un snack que te sume, no que te reste. Una fruta, un puñado de frutos secos... ¡Energía de la buena! 🍎",
        "Piensa en tu próxima comida. 🥗 ¿Cómo puedes hacerla deliciosa y súper nutritiva? Planificar es clave para no caer en tentaciones."
    ],
    "Tarde (1-5 PM)": [
        "Tu cabello es tu corona. 👑 Dedícale un minuto: un masaje suave en el cuero cabelludo o desenredarlo con cariño puede hacer una gran diferencia.",
        "¡Endereza esa espalda! Una buena postura no solo previene dolores, sino que proyecta seguridad y confianza. ¡Hombros atrás y cabeza en alto!",
        "¿Sientes el bajón de energía? ¡Es la señal perfecta para moverte! 🏃‍♀️ Vence a la pereza y regálate una dosis de vitalidad que durará toda la tarde."
    ],
    "Noche Temprana (5-7 PM)": [
        "No olvides el mejor tu sentido del humor, alista podcast o audios con chistes.",
        "Mejora tu interacción social siempre que sea posible, eso mejora tus habilidades comunicativas, recuerda que si puedes.",
        "Recuerda irte a dormir siempre dejándolo todo, la victoria de hoy es la medalla del mañana, tú lo soñaste, recuérdalo siempre."
    ],
    "Noche (7-9 PM)": [
        "El 'tú' de mañana te agradecerá esto: deja lista tu ropa de ejercicio. Es el truco definitivo para no tener excusas. 👟",
        "La batalla contra las caries se gana por la noche. Un cepillado completo con hilo dental es INNEGOCIABLE. ¡Tus dientes del futuro te lo agradecen!",
        "Tómate un momento para pensar en el día. ¿Qué hiciste bien por ti hoy? Agradece a tu cuerpo por todo lo que te permite hacer. 🙏"
    ],
    "Noche Tardía (9-10 PM)": [
        "El 'tú' de mañana te agradecerá esto: deja lista tu ropa de ejercicio. Es el truco definitivo para no tener excusas. 👟",
        "Recuerda: el progreso, no la perfección, es la meta. Cada día que lo intentas, estás ganando. ¡Estás haciendo un trabajo increíble!",
        "El sueño es la base de todo: repara músculos, consolida la memoria y embellece la piel. Asegúrate de que tu habitación esté oscura y tranquila. ¡A descansar! 😴"
    ]
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
        print(f"Hora fuera de rango ({hora_actual}:00), no se enviarán mensajes.")
        return []

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
