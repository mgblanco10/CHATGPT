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
def get_username():
    username = input("Ingrese su nombre de usuario: ")
    return username

def valid_username(username):
    # Validar si el nombre de usuario es válido o no.
    # Retornar True si es válido, de lo contrario False.

# Obtener el nombre de usuario del usuario.
username = get_username()

# Ejecutar el bucle mientras el nombre de usuario no sea válido.
while not valid_username(username):
    print("Nombre de usuario no válido.")
    username = get_username()

# El nombre de usuario es válido.
print("Nombre de usuario válido:", username)

