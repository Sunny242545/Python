def sum(a, b):
    return a + b
a = int(input("Enter first number: "))
b= int(input("Enter second number: "))
        
print(sum(a, b))


#f string in python to print the string with variables and expressions easily
def multiply(x, y):
    # ptint('x*y ='{x * y})
    print(f'x * y = {x * y}')

multiply(3, 2)

#difference between local variables and global variables in python

def twosum():
    x = int(input("Enter x value: "))
    y = int(input("Enter y value: "))
    s = x+y
    return s
print(twosum())

z = 10  # global variable

def threesum():
    x = int(input("Enter x value: "))
    y = int(input("Enter y value: "))
    s = z+x+y
    return s
print(threesum())
print(f'global variable z = {z}')
print(f'local variable x = {x}') # This will raise an error because x is not defined globally

