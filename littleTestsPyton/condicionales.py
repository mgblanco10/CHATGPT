# verdadero y falso entoncés es falso
print("Yellow">"Cyan" and "Brown">"Magenta")

# verdadero ó falso entoncés es verdadero
print("Yellow">"Cyan" or "Brown">"Magenta")

#TRUE
print(not 42 == "Answer")



print(32 == 30+2)   # The == operator checks if the 2 values are 
                    # equal to each other. If they are equal, 
                    # Python returns a True result.


print(5+10 == 6+7)  # If the two values are not equal, as in the
                    # expression 5+10 == 6+7 (or 15 == 13), Python          
                    # returns a False result.


print(10-4 != 10+4) # The != operator checks if the 2 values are
                    # NOT equal to each other. If true, Python              
                    # returns a True result. 


print(9/3 != 3*1)   # In this last example, 9/3 != 3*1 (or 3 != 3)
                    # is false. So, Python returns a False value.


# Test Example 1:

x = 2*3 > 6
print("The value of x is:")
print(x)

print("")  # Prints a blank line

print("The inverse value of x is:")
print(not x)