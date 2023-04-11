# slice
color = 'Orange'
print(color)
print(color[1:4])

fruit = 'Pineapple'
print(fruit[:4])
print(fruit[4:])

_fruit = "Mangosteen"
print(_fruit[1:4])
print(_fruit[:5])
print(_fruit[5:])
print(_fruit[:5] + _fruit[5:])

# cadenas en python son inmutables "No se pueden modificar" 
# para arreglarlo
message = "A kong string with a silly typo"
new_message = message[0:2] + "l" + message[3:]
print(message)
print(new_message)

# index method
pets = "Cats & Dogs"
print(pets.index("&"))
print("Cats" in pets)
print("Dragons" in pets)

# ejemplo
def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@"+ old_domain)
        new_email = email[:index]+ "@" + new_domain
        return new_email
    return email

# upper and lower
print("Monica".upper())
print("Monica".lower())

# espacios
print("   yes      ".strip())
print("   yes      ".lstrip())
print("   yes      ".rstrip())

# contar algún elemento
print("The number of times e occurs in this string is 4".count("e"))

# devuelve si la cadena termina con una determinada subcadena
print("Forest".endswith("rest"))

# devuelve si la cadena está formada por sólo números
print("Forest".isnumeric())
print("123456".isnumeric())
# # # # SABIENDO ESTO PODEMOS USAR FUNCIÓN int pra convertirla en un número real
print(int("12345") + int("54321"))

# concatenar
print(" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]))
print("...".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]))

# devuelve una lista de las palabras de la cadena inicial
print("This is another example".split())



