def add (a,b):
    return a + b

print(add(1,8))

add = (lambda x,y: x+y)
print(add(5,3))

square = (lambda x: x**2)
print(square(5))

is_even = lambda x:x%2==0
print(is_even(5))