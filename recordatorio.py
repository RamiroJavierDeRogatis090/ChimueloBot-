import pywhatkit
import time

jugadores = [
    ("Ramiro Javier De Rogatis", "+5491154230878")
]

for nombre, telefono in jugadores:
    mensaje = f"""
⚽ Hola {nombre}!

Soy ChimueloBot 🐉🤖

Te recuerdo que este sábado tenemos partido a las 17:00 hs.

Por favor confirmá asistencia:

✅ Voy
❌ No voy
🤔 En duda
"""

    pywhatkit.sendwhatmsg_instantly(
        telefono,
        mensaje,
        wait_time=15,
        tab_close=True
    )

    print(f"Mensaje enviado a {nombre}")
    time.sleep(10)
