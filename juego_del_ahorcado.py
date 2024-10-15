# Juego del ahorcado: elegir temario de palabra random o pedirle a un segundo jugador que ingrese una palabra.
from typing import List
import random

def eleccion_tema () -> str:
    #Podemos valdiar si es string.
    #Podemos hacer generica la eleccion de tema independiente de la cantidad de temas.
    biologia = ["MITOCONDRIA", "BIOLOGO", "MITOSIS", "NEMATODOS", "EUCARIOTA", "BACTERIA", "SIMBIOSIS"]
    peliculas = ["STARWARS"] #Se puede mejorar para reconocer espacios
    personajes = ["ARAGORN"]

    print("¡Hola! Bienvenido al juego del Ahorcado.")
    print("Elige el tema de la palabra ")
    print("1- Biologia.")
    print("2- Peliculas.")
    print("3- Personajes.")
    eligio = False

    while eligio == False:
    
        tema = input("Ingresa 1/2/3 de acurdo al tema que quieras: ")
        try:

            if tema == "1":
                return random.choice(biologia).upper()

            elif tema == "2":
                return random.choice(peliculas).upper()

            elif tema == "3":
                return random.choice(personajes).upper()
            else:
                print("Porfavor ingresa un número valido")

        except ValueError:
            print("Porfavor ingresa un número valido")

def progreso(palabra_secreta, letras_adivinadas):

    adivinado = ""
    #letr: es la letra de "palabra_secreta" en cuanto a caracteres. Empieza en posición cero.
    for letr in palabra_secreta:
        if letr in letras_adivinadas: #Evalua si la letra en la "letr" esta en letras_adivinadas
            adivinado += letr
        else:
            adivinado += "_"

    return adivinado


def juego_ahorcado():

    palabra_secreta = eleccion_tema()
    letras_adivinadas = []
    intentos = 5
    terminado = False

    print("¡Ok! ¡A jugar!")
    print(f"Tenes {intentos} intentos para adivinar la palabra.")
    print(progreso(palabra_secreta, letras_adivinadas), "La palabra es de (", len(palabra_secreta), ") caracteres.")

    while not terminado and intentos > 0:
        adivinando = input("Introduce una letra: ").upper()

        if len(adivinando) != 1 or not adivinando.isalpha():
            print("Porfavor introduzca una sola letra.")
        elif adivinando in letras_adivinadas:
            print("Ya adivinaste esa letra, intenta con otra.")
        else:
            letras_adivinadas.append(adivinando)

            if adivinando in palabra_secreta:
                print(f"¡Muy bien! ¡Has adivinado! La letra '{adivinando}' esta presente en la palabra.")
            else:
                intentos -= 1
                print(f"Lo siento, la letra '{adivinando}' no se encuentra presente en la palabra.")
                print(f"Te quedan {intentos} intentos.")

        progreso_actual = progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual)

        if "_" not in progreso_actual:
            terminado = True
            print(f"¡FELICIDADES! HAS ADIVINADO LA PALABRA '{palabra_secreta}' ;)")
            if intentos == 5:
                print("¡PERFEEEEEEECT!¡NO TE EQUIVOCASTE NI UNA VEZ!")

    if intentos == 0:
        print(f"Lo siento, se acabaron los intentos. La palabra era '{palabra_secreta}'.")
        print(" GAME OVER ... ")



juego_ahorcado()