# while specified condition is True:
#     body of loop


def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)
		n += 1

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 

#####
multiplier = 1
result = multiplier*5
while result <= 50:
  print(result)
  multiplier += 1
  result = multiplier*5
print("Done")


#####

def addition_table(given_number):
 
    iterated_number = 1
    my_sum = 1

    while iterated_number <= 5:
        my_sum = given_number + iterated_number
        if my_sum > 20:
            break

        print(str(given_number), "+", str(iterated_number), "=", str(my_sum))
        iterated_number += 1
 
 
addition_table(5)
addition_table(17) 
addition_table(30) #None > 

