x = 0 
while x < 5 :
    print ("Not there yet, x=" + str(x))
    x = x + 1
print ("x=" + str(x))

#####More while loop Examples

def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(5)


## More while
def count_down(start_number):
  while (start_number > 0):
    print(start_number)
    start_number -= 1
  print("Zero!")

count_down(3)




# More example while loop revisar ##########################
def valid_username(username):
    # Validar si el nombre de usuario es válido o no.
    # Retornar True si es válido, de lo contrario False.

    # Validar el nombre de usuario aquí y retornar True si es válido.
    # De lo contrario, retornar False.
    return True

def get_username():
    # Pedir al usuario que ingrese su nombre de usuario y retornarlo como una cadena.
    return input("Ingrese su nombre de usuario: ")

# Obtener el nombre de usuario del usuario.
username = get_username()

# Ejecutar el bucle mientras el nombre de usuario no sea válido.
while not valid_username(username):
    print("Nombre de usuario no válido.")
    username = get_username()

# El nombre de usuario es válido.
print("Nombre de usuario válido:", username)


### Otro ejemplo
starting_number = 18

while starting_number >= 0:
    print(starting_number, end=" ")
    
    starting_number -= 3


###Otro ejemplo
def X_figure(salary):
    tally = 0
    if salary == 0:
        tally += 1
    while salary >= 1:
        salary = salary/10
        tally += 1

    return tally
print("The CEO has a " + str(X_figure(2300000)) + "-figure salary.")
