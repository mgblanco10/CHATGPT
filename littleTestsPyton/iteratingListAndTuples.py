animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)

print("Total characters: {}, Average lenth: {}".format(chars, chars/len(animals)))

# La función enumerate() toma una lista como parámetro y devuelve una tupla para cada elemento de la lista.

winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))


#   ######   ########  #######   #######
def full_emails(people):
    result =[]
    for email, name in people:
        result.append("{} <{}>".format(name,email))
    return result

print(full_emails([("lulu@example.com", "Luisana Diaz"), ("gena@example.com", "Genaro Diaz"), ("monica@example.com", "Monica Blanco") ]))


# #############
def skip_elements(elements):
	
	return [element for i, element in enumerate(elements) if i % 2 == 0]

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']



#  #############    ############
def pig_latin(text):
    words = text.split()
    pig_latin_words = []
    for word in words:
        pig_latin_word = word[1:] + word[0] + "ay"
        pig_latin_words.append(pig_latin_word)
    pig_latin_text = " ".join(pig_latin_words)
    return pig_latin_text
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"



#   ########   ##########   #####
def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for digit in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if digit >= value:
                result += letter
                digit -= value
            else:
                result += "-"
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------