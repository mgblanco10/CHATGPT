def mirrored_string(my_string):
    forwards = ""
    backwards = ""

    for character in my_string:

        if character.isalpha():

            forwards += character
            backwards = character + backwards

    if forwards.lower() == backwards.lower():
        return True
    return False
 
print(mirrored_string("12 Noon")) # Should be True
print(mirrored_string("Was it a car or cat I saw")) # Should be False
print(mirrored_string("'eve, Madam Eve")) # Should be True

# #######   #######    ############    ######  #
def convert_weight(ounces):
    pounds = ounces/16 
    result = "{} ounces equals {:.2f} pounds".format(ounces,pounds)
    return result

print(convert_weight(12)) # Should be: 12 ounces equals 0.75 pounds
print(convert_weight(50.5)) # Should be: 50.5 ounces equals 3.16 pounds
print(convert_weight(16)) # Should be: 16 ounces equals 1.00 pounds


# #######   #######    ############    ######  #
def username(last_name, birth_year):

    return("{}{}".format(last_name[0:3],birth_year))

print(username("Ivanov", "1985")) 
# Should display "Iva1985" 
print(username("Rodríguez", "2000")) 
# Should display "Rod2000" 
print(username("Deng", "1991")) 
# Should display "Den1991"



def replace_date(schedule, old_date, new_date):
    if schedule.endswith(old_date):
        p = len(old_date)
        new_schedule = schedule[:-p] + schedule[-p:].replace(old_date, new_date)
        return new_schedule

    return schedule
 
 
print(replace_date("Last year’s annual report will be released in March 2023", "2023", "2024")) 
# "Last year’s annual report will be released in March 2024"
print(replace_date("In April, the CEO will hold a conference", "April", "May")) 
# "In April, the CEO will hold a conference"
print(replace_date("The convention is scheduled for October", "October", "June")) 
#  "The convention is scheduled for June"

