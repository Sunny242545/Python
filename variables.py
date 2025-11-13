# # This is a simple python print funtion with deafult string
# s = "Hello World"
# print(s)


# # This is a simple python print funtion with custom input string
# s = input("Enter a string: ")
# print("Hello "+s)


# # Comparing two strings for equality

# string1 = "Hello"
# string2 = "World"

# if string1 == string2:
#     print('two strings are equal')
# else:
#     print('two strings are not equal')

# string1 = "Hello"
# string2 = "Hello"

# if string1 == string2:
#     print('two strings are equal')
# else:
#     print('two strings are not equal')


# Comparing two strings for equality ignoring case sensitivity

# string1 = "Hello"
# string2 = "hello"

# if string1.lower() == string2.lower():
#     print('two strings are equal')
# else:
#     print('two strings are not equal')

# s="sundeep"
# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.title())
# print(s.swapcase())
# print(s.count('e'))
# print(s.find('deep'))
# print(s.replace('s','S'))
# print(s.split('e'))
# print(s.startswith('s'))
# print(s.endswith('p'))
# print(len(s))
# print(s.isalpha())
# print(s.isdigit())
# print(s.isalnum())
# print(s.index('d'))
# print(s.rindex('p'))
# print(s.center(20,'*'))
# print(s.islower())
# print(s.isupper())
# print(s.removeprefix('sun'))
# print(s.removesuffix('deep'))



# # Pattern Printing
# print(len(s))
# for i in range(1,len(s)+1):
#     print(" "*(len(s)-i)+"* "*i)

# for i in range(1,len(s)+1):
#     print("* "*i)

# for i in range(1,len(s)+1):
#     print(" "*(len(s)-i)+"*"*i)

# s="sundeep"
# #printing character at index 2
# print(s[2])
# #printing characters from 0-4
# print(s[0:5])
# #printing characters from last to first
# print(s[::-1])
# #printing characters from 2 to second last
# print("characters from 2 to second last " +s[2:-2:1])
# #printing characters from last  to second last using length function
# print("characters from last  to second last using length function " + s[len(s)-1:len(s)-3:-1])
# #printing characters from last  to second last using negative indexing
# print("characters from last  to second last " + s[-1:-3:-1])
# #printing characters from 0 to second last with step 2
# print("characters from 0 to second last with step 2 " + s[0:-1:2])

# l = ["sundeep", "kumar", "murali", "mahi", "sundeep"]
# l.append("newton")
# print(l)
# l.insert(2, "Abhi")
# print(l)
# l.remove("sundeep")
# print(l)
# l.sort()
# print(l)
# # l.reverse()
# # print(l)
# l.sort(reverse=True)
# print(l)

# list = [[0, 1], [1, 2], [2, 3]]

# print(list)
# print(list[0][0])
# print(list[1][1])

# list = []

# for i in range(3):
#     list.append([])
#     for j in range(3):
#         list[i].append(i+j)

# print(list)
# print(list[0][0])
# print(list[1][2])

# id = "xyz123"
# password = "abc@123"
# input_id = input("Enter your id: ")
# if input_id == id:
#     input_password = input("Enter your password: ")
#     for i in range(3):
#         if input_password == password:
#             print("Login Successful")
#             break
#         else:
#             print("Incorrect Password")
#             if i < 2:
#                 input_password = input("Re-enter your password: ")
#             else:
#                 print("Account Locked")
# else:
#     print("Invalid ID")

# print("welcome to the guess my age game")
# age = 25
# exit_code = 999
# guess = int(input("Guess my age: "))
# while guess != exit_code:
#     if guess < age:
#         print("Too low")
#     else:
#         print("Too high")
#     guess = int(input("Guess my age: "))

# def sum(a, b):
#     return a + b
# a = int(input("Enter first number: "))
# b= int(input("Enter second number: "))
        
# print(sum(a, b))


#f string in python to print the string with variables and expressions easily
# def multiply(x, y):
#     # ptint('x*y ='{x * y})
#     print(f'x * y = {x * y}')

# multiply(3, 2)

# difference between local variables and global variables in python

# def twosum():
#     x = int(input("Enter x value: "))
#     y = int(input("Enter y value: "))
#     s = x+y
#     return s
# print(twosum())

# z = 10  # global variable

# def threesum():
#     x = int(input("Enter x value: "))
#     y = int(input("Enter y value: "))
#     s = z+x+y
#     return s
# print(threesum())
# print(f'global variable z = {z}')
# print(f'local variable x = {x}') # This will raise an error because x is not defined globally


# x = (1,)
# y = (4,5,6)
# z = x + y
# print(z)
# x = x + y
# print(x)

# dict = {}
# dict['Ford'] = "Car"
# dict['Python'] = "The Python Programming Language"
# dict[2] = "This sentence is stored here."

# print(dict['Ford'])
# print(dict['Python'])
# print(dict[2])
# for key in dict:
#     print(f'key: {key}, value: {dict[key]}')

# x = 3
# y = 2.15315315313532

# print("We have defined two numbers,")
# print(f"x = {x}")
# print(f"y = {y}")

# a = "135.31421"
# b = "133.1112223"2

# c = float(a) + float(b)
# d = int(float(a)) + int(float(b))
# print(d)
# print(c)

# from random import random, randint
# print(random())
# print(int(random()*100))
# print(randint(1,100))

#reading the file in python
# data = open("C:\\Users\\chakr\\OneDrive\\Desktop\\sample.txt", "r")
# content = data.readlines()
# for i in content:
#     print(i, end = '')

# with open("C:\\Users\\chakr\\OneDrive\\Desktop\\sample.txt") as f:
#     lines = f.readlines()
#     for i in lines:
#         print(i, end ='')

import os.path

filepath = "C:\\Users\\chakr\\OneDrive\\Desktop\\sample.txt"

if not os.path.isfile(filepath):
    print("file does not exist")
else:
    with open(filepath, 'a+') as file:
        file.write("\nnew line by sundeep kumar ")
        file.seek(0)
        lines = file.readlines()
        for i in lines:
            print(i, end= '')








