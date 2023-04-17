# Iteración
files = {"docs":10, "slides":12, "sheets":25, "books":36}
for file in files:
    print(file)

for file, amount in files.items():
    print("In my {} I have {} this many files".format(file,amount))

print(files.keys())
print(files.values())

for value in files.values():
    print(value)

# ######## ################    ####################

def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("Hola como es esto"))
