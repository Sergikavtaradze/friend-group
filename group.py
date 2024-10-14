import copy
"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

sergi_rel = {"friends": ["Angadh", "Jonathan"], "partner":''}

angadh_rel = {"friends": ["Sergi", "Jonathan"], "partner":''}

jonathan_rel = {"friends": ["Sergi", "Angadh"], "partner": 'Tiffany'}

tiffany_rel = {"friends": "", "partner": "Jonathan"}

my_group = {"Sergi":{"age": 22 , "job": "student" , "relationship": sergi_rel},
            "Angadh":{"age": 22 , "job": "student" , "relationship": angadh_rel},
            "Jonathan": {"age": 22 , "job": "student" , "relationship": jonathan_rel},
            "Tiffany" : {"age": 24 , "job": "Analyst" , "relationship": tiffany_rel}}


def forget(storage, person1, person2):
    deep_copied = copy.deepcopy(storage)
    for name, value in deep_copied.items():
        if person1 in value["relationship"]:
            deep_copied[name]["relationship"]=value["relationship"].remove(person1)
        elif person2 in value["relationship"]:
           deep_copied[name]["relationship"]=value["relationship"].remove(person2)
    
    return deep_copied



# Jill is 26, a biologist and she is Zalika's friend and John's partner.
for row in my_group:
    print(f'{row["name"]} is {row["age"]}, (s)he is a {row["job"]} and he is friends with {row["relationship"]["friends"]} and in a romantic relationship with {row["relationship"]["partner"]}')