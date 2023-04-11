# Las tuplas son secuencias de elementos de cualquier tipo que son inmutables
# el orden no cambiará

my_name = ("Monica", "G", "Blanco")
print(my_name)

# example
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600)//60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

result = convert_seconds (5000)
print(result)
print(type(result))

# una tuple podemos Unpack (desempaquetarla)
# Esto significa que podemos convertir una tupla de tres elementos en tres variables separadas

hours, minutes, seconds = result
print(hours, minutes, seconds)

hours, minutes, seconds = convert_seconds(1000)
print(hours, minutes, seconds)

