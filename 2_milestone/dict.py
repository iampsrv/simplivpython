# my_dict = {"name": "Pranjal", "age": 26, "city": "Pune", "skills":["pyhton","java","c","aws"]}
# my_dict["name"]="Pranjal Srivastava"
# my_dict["contact"]=77777777
# print(my_dict)
# keys = my_dict.keys()
# print(keys)

# values = my_dict.values()
# print(values)


dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "country": "USA"}
merged_dict = {**dict1, **dict2}

print(merged_dict)