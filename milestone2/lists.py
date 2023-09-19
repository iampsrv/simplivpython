# my_list = ['apple', 'banana', 'cherry']
# # print(my_list[1])
# # print(my_list[-2])
# my_list[0] = 'orange'
# my_list.append('mango')
# my_new_list = ['grapes', 'kiwi']
# # my_list.extend(my_new_list)
# merged_list = my_list + my_new_list
# # print(merged_list)

# # # list_of_employees = ["Pranjal","Maxwell", "James","Paul","Jason","Bravo"]

# # # print(list_of_employees[0])

# # print(merged_list[1:3]) # Slicing from index 1 to 2 ([2, 3])
# # print(merged_list[:3]) # Slicing from the beginning to index 2 ([1, 2, 3])
# # print(merged_list[2:])

# # merged_list.remove('banana') # Removing a specific element
# # del merged_list[0] # Removing element at index 0
# # merged_list.pop()
# # print(len(merged_list))
# # 
# # 
# if 'mango' in merged_list:
#     print("Found!")
# else:
#     print("Not found")

# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(nested_list[2][1])

# my_list = [1, 2, 3, 4, 5]
# my_list.insert(2, 10) # Inserting the value 10 at index 2
# print(my_list)

marks = [90,100,80]
sub = ["Maths","Sci","History"]
for fruit,price in zip (sub,marks):
     print(fruit,price)
print("Average Marks",sum(marks)/len(sub))