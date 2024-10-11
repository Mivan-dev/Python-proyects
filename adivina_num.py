# Adivina un numero del 1 al 100 en maximo 5 intentos o pide vida extra, 2 intentos mas, aunque no se si lo mereces.

# import random

# def adivinanza():
    
#     num_adivinar = random.randint(1, 100)
#     intento = 1
#     adivina = False
#     vida = 5

#     print("¡Hola! ¿Queres jugar a la adivinanza?")
#     print("Adivina un numero del 1 al 100.")
        
#     while not adivina and vida > 0:

#         numero = int(input(f"Intento {intento}: Introduzca un digito  "))
#         intento += 1
#         vida -= 1

#         if numero > num_adivinar:
#             print("El numero es menor ;)")

#         elif numero < num_adivinar:
#             print("El numero es mayor ;)")

#         else:
#             print("¡Felicitaciones! Adivinaste el numero secreto de la secretidad :)")
#             adivina = True

#         if vida == 0:

#             print("Lo siento, se te acabaron los intentos. ¡Perdedor!")
#             sigue = input("¿Quieres seguir jugando? Te ofrezco 2 intentos mas: si/no  ")
            
#             if sigue.lower() == "si":
#                 vida += 2
#             else:
#                 print("Ok, adios salame.")
#             adivina = True

# adivinanza()

import random

def adivinanza():
    num_adivinar = random.randint(1, 100)
    intento = 1
    adivina = False
    vida = 5
    extra = 1
    sigue = "no"

    print("¡Hola! ¿Quieres jugar a la adivinanza?")
    print("Adivina un número del 1 al 100.")
        
    while not adivina:  # Cambiar la condición del bucle
        if vida > 0:  # Solo se solicita un número si hay vidas restantes
            try:
                numero = int(input(f"Intento {intento}: Introduzca un dígito: "))
                intento += 1
                vida -= 1

                if numero > num_adivinar:
                    print("\nEl número es menor ;)\n")

                elif numero < num_adivinar:
                    print("\nEl número es mayor ;)\n")

                else:
                    print("¡Felicitaciones! Adivinaste el número secreto de la secretidad :)")
                    adivina = True  # El juego termina aquí si se adivina

            except ValueError:
                print("Por favor, ingrese un número válido.")
                continue  # Vuelve al inicio del bucle

        else:  # Cuando se acaban las vidas
            print("Lo siento, se te acabaron los intentos. ¡Perdedor!")

            if extra > 0:
                sigue = input("¿Quieres seguir jugando? Te ofrezco 2 intentos más: si/no: ")
            else:
                print("Adiós salame.")
                adivina = True  # Aquí se termina el juego si el usuario dice "no"
                print(f"El numero secreto de la secretidad era el ¡{num_adivinar}!")
                
            if sigue.lower() == "si":
                vida += 2  # Añadimos 2 intentos más
                # No se cambia `adivina` a True, por lo que el bucle continuará
                extra -= 1
            else:
                print("Adiós salame.")
                adivina = True  # Aquí se termina el juego si el usuario dice "no"
                print(f"El numero secreto de la secretidad era el ¡{num_adivinar}!")

adivinanza()