import pywhatkit
import time

jugadores = [
    ("Ramiro Javier De Rogatis", "+5491154230878"),
    ("Nicolas Jesus Ares", "+5491123677611"),
    ("Leonel Maximiliano Fernández Bravo", "+5491125243994"),
    ("Angel Renato Peñaranda Alcaraz", "+5491156219369"),
    ("Nehuen Lautaro Hernández", "+5491136869963"),
    ("Franco Caballero", "+5491166775580"),
    ("Juani Ignacio Mercuri (Chiche)", "+5491156373834"),
    ("Ariel Daniel Ramos Quispe", "+5491122517448"),
    ("Jorge Flores", "+5491125194559"),
    ("Tiago Nahuel Pujia", "+5491135201875"),
    ("Sebastián Gabriel Petrullo", "+5491170243941"),
    ("Diego Mario Ezequiel Ponce De Leon", "+5491133770540"),
    ("Aldrin Yasser Romero Gonzáles", "+5491125620012"),
    ("Lucas Gabriel Sánchez", "+5491136440742"),
    ("Nahuel Dario Falce Mendoza (LYO)", "+5491154850108"),
    ("Jose Luis Ignacio (Atahualpa)", "+5491170969187")
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