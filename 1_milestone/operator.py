'''
quantity = 50
price = 100

total = quantity*price

discount = 2
print("total amount is ", total-discount)
'''

# number_1 = 50
# number_2 = 51
# number_3=52

if number_2>number_1 and number_3<number_2:
    print("condition met")
else:
    print("condition not met")


# number_1 = 50
# # number_1 = number_1 * 50
# number_1*=50
# print(number_1)

# skills = ["python","java"]
# my_skills = ["c","java"]
# print(skills)
# print(my_skills)

# # print(skills is my_skills)

# print("aws" in skills)


# def dtb(num):
#     if num>=1:
#         dtb(num // 2)
#     print(num % 2, end = '')

def DecimalToBinary(num):
	
	if num >= 1:
		DecimalToBinary(num // 2)
	print(num % 2)

# Driver Code
if __name__ == '__main__':
	
	# decimal value
	dec_val = 61
	
	# Calling function
	DecimalToBinary(dec_val)


a = 60
b =13
c= a|b

print(c)
