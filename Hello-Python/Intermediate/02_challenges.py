# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=4142

### Challenges ###

"""
EL FAMOSO "FIZZ BUZZ”:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""
print("Fizz Buzz")

def fizz_buzz():
  for i in range(1, 101):
    if (i % 3 == 0) and (i % 5 == 0):
      print("fizzbuzz")
    elif i % 3 == 0:
      print("fizz")
    elif i % 5 == 0:
      print("buzz")
    else:
      print(i)

fizz_buzz()

"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""
print()
print("Anagrama")

def anagrama(palabra1, palabra2):
  if palabra1.lower() == palabra2.lower():
    return False
  else:
    return sorted(palabra1.lower()) == sorted(palabra2.lower())
print(anagrama("amor", "roma"))
#pasamos todas las letras a minuscula, luego el sorted las reordena de forma alfabetica y compara

"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""
print()
print("Fibonacci")
def fibonacci():
  init = 0
  next = 1
  for i in range(0, 50):
    print(f"{i}. {init}")
    fibo = init + next
    init = next
    next = fibo
    
fibonacci()
"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""
print()
print("Numeros primos")

def prime():
  for number in range(1, 101):
    if number >= 2:
      divisible = False
      for i in range (2, int(number**0.5) + 1): #Comprobamos divisibilidad solo hasta la raíz cuadrada de n
        if number % i == 0:
          divisible = True
          break
      if not divisible:
        print(number)   
        
prime()

"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""
print()
print("Invertir cadenas")

def invert(string):
  new_string = len(string) # new_string == 13
  revers = ""
  for i in range(0, new_string): # recorre con la variable i dentro del rango(0, 13), pero recordar que siempre excluye al ultimo (0, 12)
    revers += string[new_string - i - 1] 
    # revers += string[13 - 0 - 1] --> revers += string[12]
    # revers += string[13 -1 -1] --> revers += string[11]
    # revers += string[13 -2 -1] --> revers += string[10]
    return revers 
#  si quitamos el -1 de [13 - 0 - 1],esto es incorrecto porque el índice 13 está fuera de los límites de la cadena, índices válidos 0 a 12

print(invert("Buenas Tardes"))

