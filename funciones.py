import math
import numpy as np

def suma(num_1: float, num_2: float) -> float:

    """Suma dos nùmeros flotantes

    Args:
        num_1 (float): primer numero para ser sumado
        num_2 (float): Segundo numero para ser sumado

    Returns:
        float: Resultado de la suma de los nùmeros anteriores
    """
    valor_suma: float = num_1 + num_2
    return valor_suma

#Ejercicio: Escribir una función que muestre por pantalla 'Hola Mundo'

def hola_mundo() -> None:
    print('Hola Mundo')

##Ejercicio: Escribir una función que reciba el nombre de una persona y muestre por pantalla 'Hola (nombre)' 

def saludo(nombre:str) -> None:
    
    saludo = f"Hola {nombre}"
    print(saludo)

saludo('Pepito')

#Escribir una fución que reciba un número entero y devuelva su factorial. nótese que esta funci´pon si tiene return


def factorial(numero: int) -> int:
    """Esta funciòn calcula el factorial de un número dado

    Args:
        numero (int): número para tener facvtorial

    Returns:
        int: Valor del factorial
    """
    numero_factorial = math.factorial(numero)
    return numero_factorial

#Escribir una funciòn que reciba una lista de números y retorne su media

def mean(arrayList:list):
  return (np.array(arrayList)).mean()

def media(lista_numeros: list) -> float:
    media_valores = sum(lista_numeros)/len(lista_numeros)

