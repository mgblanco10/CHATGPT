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
