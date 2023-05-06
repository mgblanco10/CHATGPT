def greeting(name):
    print("Welcome, "+ name)

greeting("Moni")
greeting("Gena")
greeting("Lu")

def _greeting(name, department):
    print("Welcome, "+ name)
    print("You are part of "+ department)


_greeting("Moni", "adulto")
_greeting("Gena", "adulto")
_greeting("Lu", "niña")

def area_triengle(base, heigth):
    return base * heigth/2

area_a = area_triengle(5, 4)
area_b = area_triengle(7, 3)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum))

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

# ojo print(result) es none 
def saludo(name):
    print("Hola " + name)

result = saludo("Monica")
print(result)

nombre = "Kay"
numero = len(nombre)*9
print("Hola "+ nombre + " tú número de la suerte es "+ str(numero))

nombre = "Cameron"
numero = len(nombre)*9
print("Hola "+ nombre + " tú número de la suerte es "+ str(numero))

# Una funcion que agrupe los dos scripts anteriores
def numero_suerte (nombre):
    numero = len(nombre)*9
    print ("Ahora esta función es la que ejecuta el número de la suerte según la cantidad de letras del nombre "+ str(numero))

numero_suerte("Pa")
numero_suerte("Toto")

