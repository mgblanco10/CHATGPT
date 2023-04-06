# def recursive_function(parameters):
#     if base_case_condition(parameters):
#         return base_case_value
#     recursive_function(modified_parameters)


def factorial (n):
    print("Factorial called with "+ str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n-1)
    print ("Returning "+ str(result)+ " for factorial of "+ str(n))
    return result

factorial(4)

def _factorial (n):
    if n < 2:
        return 1
    return n * _factorial (n -1)
print(_factorial(100))


def count_by_10(end):
    count = ""
    for number in range(0,end+1,10):
        count += str(number) + " "
    return count.strip()
print(count_by_10(100))

def matrix(initial_number, end_of_first_row):
    n1 = initial_number 
    n2 = end_of_first_row+1  # include the upper range value with +1
    for column in range(n1, n2):
        for row in range(n1, n2):
            print(column*row, end=" ")
        print()

matrix(1, 4)
