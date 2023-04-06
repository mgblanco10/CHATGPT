# for variable in sequence:
#     body of loop

for left in range (7):
    for right in range (left, 7):
        print("["+ str(left)+ "|" + str(right)+"]", end=" ")
    print()

teams = [ 'Dargons', 'Tigers', 'Pandas', 'Unicorns']

for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)

for x in [25]:
    print(x)

def greet_friends(friends):
    for friend in friends:
        print("Hello "+ friend)

greet_friends(['Mónica', 'Genaro', 'Javier', 'Luisana'])


# This loop iterates on the value of the "number" variable in a range
# of 1 to 6+1 (the upper range limit of 6 is excluded, so +1 has
# been added to it to include 6 in the range). The incremental value
# for the loop is 2 (number+2). The print() function will output the
# resulting value of "number" multiplied by 3.
for number in range(1,6+1,2):
    print(number*3)
# The loop should print 3, 9, 15



# This loop iterates on the value of the "number" variable in a range
# of 2 to 7 (the upper range limit of 8 is excluded). The print() 
# function will output the resulting value of "number" squared.
for number in range(2,8):
    print(number**2)
# The loop should print 4, 9, 16, 25, 36, 49


for x in range(2):
    print("This is the outer loop iteration number " + str(x))
    for y in range(3+1):
        print("Inner loop iteration number " + str(y))
    print("Exit inner loop") 


for k in range(7):
    if k % 2 == 0:
        print(k)



