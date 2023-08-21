for i in range (1,20):
    if i%2==0:
        print(i**2)

squares = [x ** 2 for x in range(1,20) if x%2==0]
print(squares)