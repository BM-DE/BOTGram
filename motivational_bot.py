import random
import requests
import os
from datetime import datetime
import pytz

# Configuración desde variables de entorno
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

# Mensajes por categoría y área
mensajes = {
    "Mañana Temprano (7-9 AM)": [
        "Hoy es un día para construir. Cada línea de código es un ladrillo de tu futuro. ¿Cuál es la primera tarea que vas a demoler?",
        "No pienses en 'ganar dinero'. Piensa en 'resolver problemas'. El dinero es la recompensa por el valor que creas. ¿Qué problema vas a resolver hoy?",
        "La disciplina es el puente entre tus metas y tus logros. Cierra las distracciones, abre el editor de código. ¡Vamos!",
        "Recuerda tu 'porqué'. No es solo por el dinero, es por la libertad, la independencia y el respeto propio. Cada git commit te acerca a eso.",
        "La procrastinación es el ladrón de tus sueños. La acción es la llave. ¿Qué vas a hacer en los próximos 25 minutos para avanzar? (Técnica Pomodoro: https://pomofocus.io/)"
    ],
    "Media Mañana (9-11 AM)": [
        "¿Atascado en un bug? ¡Perfecto! No es un error, es una lección de lógica. Tómate un respiro de 10 minutos, mira el problema con ojos frescos y atácalo de nuevo. Puedes usar https://rubberduckdebugging.com/.",
        "Revisa tu portafolio. ¿El proyecto que estás construyendo hoy te haría sentir orgulloso de mostrarlo en una entrevista? Si no, ¿qué puedes mejorar?",
        "El conocimiento es poder. Dedica 30 minutos a un tutorial de esa tecnología que te intimida. Hoy, esa intimidación se convierte en habilidad. Busca '[nombre de la tecnología] tutorial' en YouTube.",
        "Recuerda: 'Hecho' es mejor que 'perfecto'. Avanza, itera, mejora después. No te quedes paralizado buscando la perfección inicial."
    ],
    "Mediodía (11 AM-1 PM)": [
        "Tu cuerpo es el vehículo de tus ambiciones. ¿Ya lo moviste hoy? 30 minutos de ejercicio valen más que 3 horas de autocompasión. Sal a caminar, haz unas flexiones. ¡Ahora!",
        "La confianza no se encuentra, se construye. Hoy vas a hacer una cosa que te dé un poco de miedo. Hablar con un desconocido o intentar algo nuevo. La acción cura el miedo.",
        "La postura de poder: Levanta la cabeza, hombros hacia atrás. Camina como si ya fueras el hombre en el que te quieres convertir. El cuerpo le enseña a la mente."
    ],
    "Tarde (1-5 PM)": [
        "¡Hora de inspirarte! Cada paso te acerca a tus sueños. Dedica 15 minutos a planificar tu próximo proyecto.",
        "Tu voz importa. Practica una conversación hoy con alguien nuevo. La confianza crece con la acción.",
        "Tip de estilo rápido: ¿Tu ropa está limpia y te queda bien? 5 minutos para elegir tu look de mañana envían un mensaje grande."
    ],
    "Noche Temprana (5-7 PM)": [
        "¿Qué aprendiste hoy? Anótalo. El conocimiento acumulado es tu mayor activo. Usa Notion para tu 'diario de programador'.",
        "Misión cumplida por hoy. Cierra la laptop sintiéndote orgulloso. El descanso consolida lo aprendido.",
        "Mañana serás mejor. El interés compuesto de tus habilidades empieza ahora. ¡Bien hecho!"
    ],
    "Noche (7-9 PM)": [
        "La persona más interesante en la habitación escucha. Hoy, haz preguntas y conecta de verdad con alguien.",
        "Hoy es un buen día para salir de la cueva. Trabaja una hora desde una cafetería y observa a la gente.",
        "Tu cuerpo necesita movimiento. 20 minutos de estiramiento antes de dormir mejoran tu energía."
    ],
    "Noche Tardía (9-10 PM)": [
        "El programador ya trabajó. Ahora es el turno del músico. Coge tu guitarra y toca, es tu recompensa.",
        "¿Frustrado? Convierte esa energía en un blues con tu guitarra. La música procesa emociones.",
        "Practica esa escala difícil 15 minutos. Mañana será más fácil. Usa https://www.ultimate-guitar.com/."
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

def seleccionar_mensajes():
    lima_tz = pytz.timezone('America/Lima')
    hora_actual = datetime.now(lima_tz).hour
    print(f"Hora detectada en Lima: {hora_actual}:00")

    if 7 <= hora_actual < 9:  # 7:00 AM - 8:59 AM
        return ["Mañana Temprano (7-9 AM)"] * 3
    elif 9 <= hora_actual < 11:  # 9:00 AM - 10:59 AM
        return ["Media Mañana (9-11 AM)"] * 3
    elif 11 <= hora_actual < 13:  # 11:00 AM - 12:59 PM
        return ["Mediodía (11 AM-1 PM)"] * 3
    elif 13 <= hora_actual < 17:  # 1:00 PM - 4:59 PM
        return ["Tarde (1-5 PM)"] * 3
    elif 17 <= hora_actual < 19:  # 5:00 PM - 6:59 PM
        return ["Noche Temprana (5-7 PM)"] * 3
    elif 19 <= hora_actual < 21:  # 7:00 PM - 8:59 PM
        return ["Noche (7-9 PM)"] * 3
    elif 21 <= hora_actual < 22:  # 9:00 PM - 9:59 PM
        return ["Noche Tardía (9-10 PM)"] * 3
    else:
    print(f"Hora fuera de rango ({hora_actual}:00), enviando mensaje de prueba.")
    return ["Mañana Temprano (7-9 AM)"] * 3

def main():
    if not BOT_TOKEN or not CHAT_ID:
        print("Error: Faltan token o chat ID")
        return
    categorias = seleccionar_mensajes()
    if categorias:
        for categoria in categorias:
            mensaje = random.choice(mensajes[categoria])
            print(f"Mensaje: {mensaje}")
            resultado = enviar_mensaje_telegram(mensaje)
            if resultado and resultado.get('ok'):
                print("Mensaje enviado con éxito")
            else:
                print("Fallo al enviar mensaje")
    else:
        print("No hay categorías para esta hora.")

if __name__ == "__main__":
    main()
