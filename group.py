import copy
import statistics
import numpy as np
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

# Add some code that makes use of comprehension expressions to your group.py file so that it prints out the following when the script is run:
# the maximum age of people in the group
# the average (mean) number of relations among members of the group
# the maximum age of people in the group that have at least one relation
# [more advanced] the maximum age of people in the group that have at least one friend

max_age = max([values["age"] for name, values in my_group.items()])
avg_relations = np.mean([len(values["relationship"]) for name, values in my_group.items()])
max_age_w_friend = max([values["age"] for name, values in my_group.items() if len(values["relationship"]["friends"]) > 0])

print(f'This is the max age {max_age}, the mean relations {avg_relations}, blabla {max_age_w_friend}')

# Jill is 26, a biologist and she is Zalika's friend and John's partner.
# for row in my_group:
#     print(f'{row["name"]} is {row["age"]}, (s)he is a {row["job"]} and he is friends with {row["relationship"]["friends"]} and in a romantic relationship with {row["relationship"]["partner"]}')