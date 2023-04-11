# Las comprensiones de listas nos permiten crear nuevas listas basadas en secuencias o rangos.

multiples = []
for x in range (1, 11):
    multiples.append(x*7)

print(multiples)

multiples = [x*7 for x in range(1, 11)]
print(multiples)

#  ######## #####
languages = ["Python", "Perl", "Ruby", "Js", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)


#  ################# ##############  ###############
z = [x for x in range(0, 101) if x % 3 == 0]
print(z)

#   ####### ######## 
def odd_numbers(n):
	return [x for x in range (1, n + 1) if x % 2 !=0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []


#  ######

print("List comprehension result:")
print([x*2 for x in range(1,11)]) 

print("Long form code result:")

my_list = []
for x in range(1,11):
   my_list.append(x*2)
print(my_list)


# ### ########################### #######
print("List comprehension result:")

print([ x for x in range(1,101) if x % 10 == 0 ])

print("Long form code result:")

my_list = []
for x in range(1,101):
  if x % 10 == 0:
    my_list.append(x)
print(my_list)


# more examples
def squares(start, end):
      return [x*x for x in range(start, end+1)]


print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


