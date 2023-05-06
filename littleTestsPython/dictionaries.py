x = {}
print(type(x))
file_count ={"jpg":10, "csv":2, "py":23}
print(file_count)
print(file_count["jpg"])
print("jpg" in file_count)
print("html" in file_count)
file_count["txt"]= 8
print(file_count)
# ojo cuando se utiliza una key existente reemplaza el valor
file_count["txt"]= 123
print(file_count)
# eliminar elementos 
del file_count["txt"]
print(file_count)

# my_dictionary = {keyA:value1,value2, keyB:value3,value4}
animals = { "bears":23, "lions": "diez", "birds":["dos", 3, "cuatro"], "tigers":2 } 
print(animals)
print(animals["lions"])
print("bears" in animals)
animals["zebras"] = 2
print(animals)

pet_dictionary = {"dogs": ["Yorkie", "Collie", "Bulldog"], "cats": ["Persian", "Scottish Fold", "Siberian"], "rabbits": ["Angora", "Holland Lop", "Harlequin"]}  
print(pet_dictionary.get("dogs", 0))

pet_list  = ["Yorkie", "Collie", "Bulldog", "Persian", "Scottish Fold", "Siberian", "Angora", "Holland Lop", "Harlequin"]
print(pet_list[0:2])

#  #### ########
def sum_server_use_time(Server):
    total_use_time = 0.0
    for key,value in Server.items():
        total_use_time += Server[key]
    return round(total_use_time, 2)  

FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
print(sum_server_use_time(FileServer)) # Should print 20.1

# ######## ########### ########

def list_full_names(employee_dictionary): 
    full_names = []
    for last_name, first_names in employee_dictionary.items():
        for first_name in first_names:
            full_names.append(first_name+" "+last_name)
    return(full_names)

print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}))

# ###### ########### ##########
def invert_resource_dict(resource_dictionary):
    new_dictionary = {}
    for resource_group, resources in resource_dictionary.items():
        for resource in resources:
            if resource in new_dictionary:
                new_dictionary[resource].append(resource_group)
            else:
                new_dictionary[resource] = [resource_group]
    return(new_dictionary)

print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
        "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"],
        "Video Cards": ["High-end video cards", "Basic video cards"]}))