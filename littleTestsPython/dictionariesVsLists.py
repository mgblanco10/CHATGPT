ip_addresses = ["192.168.1.1", "127.0.0.1", "8.8.8.8"]

host_address = { "router": "192.168.1.1", "localhost":"127.0.0.1", "google":"8.8.8.8"}
# my_dictionary = {keyA:value1,value2, keyB:value3,value4}

# Methods
# dictionary.get(key, default) - Returns the value corresponding to a key, or the default value if the specified key is not present.
# dictionary.keys() - Returns a sequence containing the keys in a dictionary.
# dictionary.values() - Returns a sequence containing the values in a dictionary.
# dictionary[key].append(value) - Appends a new value for an existing key.
# dictionary.update(other_dictionary) - Updates a dictionary with the items from another dictionary. Existing entries are updated; new entries are added.
# dictionary.clear() - Deletes all items from a dictionary.
# dictionary.copy() - Makes a copy of a dictionary.

pet_dictionary = {"dogs": ["Yorkie", "Collie", "Bulldog"], "cats": ["Persian", "Scottish Fold", "Siberian"], "rabbits": ["Angora", "Holland Lop", "Harlequin"]}  
print(pet_dictionary.get("dogs", 0))


def list_full_names(employee_dictionary): 
    full_names = []
    for last_name, first_names in employee_dictionary.items():
        for first_name in first_names:
            full_names.append(first_name+" "+last_name) 
    return(full_names)


print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}))
# Should print ['Muhammad Ali', 'Amir Ali', 'Malik Ali', 'Ram Devi', 'Amaira Devi', 'Feng Chen', 'Li Chen']

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
# Should print {'IDE HDDs': ['Hard Drives', 'PC Parts'], 'SCSI HDDs': ['Hard Drives', 'PC Parts'],
#  'High-end video cards': ['PC Parts', 'Video Cards'], 
# 'Basic video cards': ['PC Parts', 'Video Cards']}

