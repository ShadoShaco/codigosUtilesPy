menu = """
TODO ESTE TEXTO VA A ESTAR COMENTADO
"""

-------------------------------------
nombre = nombre.capitalize() #shaco -> Shaco
nombre = nombre.strip() #sin espacios al inicio ni al final
nombre = nombre.uppercase() #shaco -> SHACO
nombre.lower(shaco)
nombre.replace("o","a") #de masculino a femenino

-------------------------------------

https://manytools.org/hacker-tools/convert-images-to-ascii-art/

-------------------------------------
#numeros primos

def es_primo(numero):
    contador = 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False


def run():
    numero = int(input('Escribe un número: '))
    if es_primo(numero):
        print('Es primo')
    else:
        print('No es primo')

-------------------------------------
#Adivina el número
import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un número del 1 al 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un número más grande')
        else:
            print('Busca un número más pequeño')
        numero_elegido = int(input('Elige otro número: '))
    print('¡Ganaste!')

-------------------------------------
#potencias
def run():
    
    for i in range(100):
        potencia_2 = 2**i
        print('2 elevado a ' + str(i) +
              ' es igual a: ' + str(potencia_2))
        i+=1

-------------------------------------
#Buscar primos
def es_primo(numero):
    contador = 0
    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return numero
    else:
        return False


def run():
    for numero in range(10000):
        if es_primo(numero):
            print(str(numero))
