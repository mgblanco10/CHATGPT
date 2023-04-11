x = ["Now", "we", "are", "cooking!"]
print(x)
print(type(x))
print(len(x))
print("are" in x)
print("Today" in x)
print(x[0])
print(x[1:3])
print(x[:2])
print(x[2:])


def get_word(sentence, n):
    # Only proceed if n is positive
    if n > 0:
        words = sentence.split()  # Split the sentence into words
        # Only proceed if n is not more than the number of words
        if n <= len(words):
            return words[n - 1]  # Return the nth word (subtract 1 to account for 0-based indexing)
    return ""

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing


# ##### ###### ###### ####### Metodos listas
#Modifying the contents of a list
fruits = ["Pineapple", "Banana", "Apple", "Mango"]
print(fruits)

fruits.append("Kiwi")
print(fruits)

fruits.insert(0, "Melon")
print(fruits)

##OJO Si agregamos un número mayor que la logitud simplemente se agregará al final
fruits.insert(25, "Orange")
print(fruits)

#remove si el elmento no lo encuentra es un ValueError
fruits.remove("Melon")
print(fruits)
