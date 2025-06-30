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
    "Inicio del Día (8-9 AM)": [
        "Hoy es un día para construir. Cada línea de código es un ladrillo de tu futuro. ¿Cuál es la primera tarea que vas a demoler?",
        "No pienses en 'ganar dinero'. Piensa en 'resolver problemas'. El dinero es la recompensa por el valor que creas. ¿Qué problema vas a resolver hoy?",
        "La disciplina es el puente entre tus metas y tus logros. Cierra las distracciones, abre el editor de código. ¡Vamos!",
        "Recuerda tu 'porqué'. No es solo por el dinero, es por la libertad, la independencia y el respeto propio. Cada git commit te acerca a eso.",
        "La procrastinación es el ladrón de tus sueños. La acción es la llave. ¿Qué vas a hacer en los próximos 25 minutos para avanzar? (Técnica Pomodoro: https://pomofocus.io/)"
    ],
    "Mediodía (1 PM)": [
        "¿Atascado en un bug? ¡Perfecto! No es un error, es una lección de lógica. Tómate un respiro de 10 minutos, mira el problema con ojos frescos y atácalo de nuevo. Puedes usar https://rubberduckdebugging.com/ para explicar el problema en voz alta.",
        "Revisa tu portafolio. ¿El proyecto que estás construyendo hoy te haría sentir orgulloso de mostrarlo en una entrevista? Si no, ¿qué puedes mejorar?",
        "El conocimiento es poder. Dedica 30 minutos de tu almuerzo a ver un tutorial sobre esa tecnología que te intimida. Hoy, esa intimidación se convierte en habilidad. Sugerencia: Busca '[nombre de la tecnología] tutorial' en YouTube.",
        "Recuerda: 'Hecho' es mejor que 'perfecto'. Avanza, itera, mejora después. No te quedes paralizado buscando la perfección inicial."
    ],
    "Fin de Jornada (6-7 PM)": [
        "¿Qué aprendiste hoy? No importa si fue mucho o poco. Anótalo. El conocimiento acumulado es tu mayor activo. Puedes usar una simple app de notas o una herramienta como Notion para tu 'diario de programador'.",
        "Misión cumplida por hoy. Cierra la laptop sintiéndote orgulloso del esfuerzo. El descanso es parte del proceso. Tu cerebro necesita tiempo para consolidar lo aprendido.",
        "Mañana serás un poco mejor que hoy. Ese es el poder del interés compuesto aplicado a tus habilidades. ¡Bien hecho!"
    ],
    "Desarrollo Personal (1-9 PM)": [
        "La confianza no se encuentra, se construye. Hoy vas a hacer una cosa que te dé un poco de miedo. Hablar con un desconocido, ir al gimnasio, subir un video tocando la guitarra. La acción cura el miedo.",
        "Tu cuerpo es el vehículo de tus ambiciones. ¿Ya lo moviste hoy? 30 minutos de ejercicio valen más que 3 horas de autocompasión. Sal a caminar, haz unas flexiones. ¡Ahora!",
        "La postura de poder: Levanta la cabeza, hombros hacia atrás. Camina como si ya fueras el hombre en el que te quieres convertir. El cuerpo le enseña a la mente.",
        "Hoy es un buen día para salir de la cueva. Trabaja una hora desde una cafetería. Observa a la gente. Acostúmbrate a estar en el mundo, no solo a verlo desde una pantalla.",
        "Tip de estilo rápido: ¿Tu ropa te queda bien? ¿Está limpia? ¿Tus zapatillas están decentes? Son detalles pequeños que envían un mensaje grande. Tómate 5 minutos para elegir qué te pondrás mañana.",
        "La persona más interesante en la habitación es la que más se interesa por los demás. Cuando hables con alguien, haz preguntas y escucha de verdad."
    ],
    "Guitarra (10-12 PM)": [
        "El programador ya trabajó. Ahora es el turno del músico. Coge tu guitarra. No para 'practicar', sino para 'tocar'. Siente la música. Es tu recompensa del día.",
        "¿Frustrado con el código? Traduce esa frustración en un blues en la guitarra. La música es la mejor forma de procesar emociones.",
        "Hoy no compites contra nadie, solo contra tus propios dedos. Practica esa escala o ese acorde que te cuesta durante 15 minutos sin parar. Mañana será más fácil. Herramienta: https://www.ultimate-guitar.com/ para encontrar tablaturas de lo que sea.",
        "Grábate tocando una canción, aunque sea con el móvil y solo para ti. Escucharte es la forma más rápida de mejorar.",
        "Busca un 'open mic' o 'micro abierto' cerca de ti en Google Maps. No para ir hoy, solo para saber dónde están. Un día, entrarás por esa puerta. Hoy, solo das el primer paso de encontrarla.",
        "La guitarra es tu superpoder social. Imagina la escena: estás en una reunión, hay una guitarra, y tú sabes qué hacer con ella. Cada minuto que tocas hoy te acerca a ese momento."
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
    print(f"Hora en Lima: {hora_actual}:00")

    if 8 <= hora_actual < 10:  # 8:00 AM - 9:59 AM
        return ["Inicio del Día (8-9 AM)"] * 2  # 2 mensajes de esta categoría
    elif 13 <= hora_actual < 14:  # 1:00 PM - 1:59 PM (aproximado para Mediodía)
        return ["Mediodía (1 PM)"] * 2  # 2 mensajes de esta categoría
    elif 18 <= hora_actual < 20:  # 6:00 PM - 7:59 PM (Fin de Jornada)
        return ["Fin de Jornada (6-7 PM)"] * 2  # 2 mensajes de esta categoría
    elif 13 <= hora_actual < 22:  # 1:00 PM - 9:59 PM (Desarrollo Personal)
        return ["Desarrollo Personal (1-9 PM)"] * 2  # 2 mensajes de esta categoría
    elif 22 <= hora_actual < 24:  # 10:00 PM - 11:59 PM (Guitarra)
        return ["Guitarra (10-12 PM)"] * 2  # 2 mensajes de esta categoría
    else:
        return ["Desarrollo Personal (1-9 PM)"] * 2  # Por defecto hasta las 12 AM

def main():
    if not BOT_TOKEN or not CHAT_ID:
        print("Error: Faltan token o chat ID")
        return
    categorias = seleccionar_mensajes()
    for categoria in categorias:
        mensaje = random.choice(mensajes[categoria])
        print(f"Mensaje: {mensaje}")
        resultado = enviar_mensaje_telegram(mensaje)
        if resultado and resultado.get('ok'):
            print("Mensaje enviado con éxito")
        else:
            print("Fallo al enviar mensaje")

if __name__ == "__main__":
    main()
