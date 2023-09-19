# my_dict = {"name": "Pranjal", "age": 26, "city": "New York"}
# print(my_dict["name"])


employees = [
    {"name": "Pranjal", "age": 26, "city": "New York", "skills":["python","java"]},
    {"name": "Bravo", "age": 30, "city": "London", "skills":("python")},
    {"name": "Harshit", "age": 29, "city": "Seatle", "skills":["java"]}
]
# print(employees)
# employees[2]['skills'][0] = "Machine Learning"
print(employees[0]['skills'])

# dict1 = {"name": "Alice", "age": 25}
# dict2 = {"city": "New York", "country": "USA"}
# merged_dict = {**dict1, **dict2}
# print(merged_dict)