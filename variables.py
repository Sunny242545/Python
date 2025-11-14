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

# import os.path

# filepath = "C:\\Users\\chakr\\OneDrive\\Desktop\\sample.txt"

# if not os.path.isfile(filepath):
#     print("file does not exist")
# else:
#     with open(filepath, 'a+') as file:
#         file.write("\n I love Mahi ")
#         file.seek(0) #with a+ mode my file pointer is at the end of the file so to read the file we need to set the pointer to the begining of the file
#         lines = file.readlines()
#         for i in lines:
#             print(i, end= '')

#working on classes and objects in python

# class Progressreport:
#     physicspassmarks = 40

#     def __init__(self, name, maths, physics):
#         self.name = name
#         self.maths = maths
#         self.physics = physics

#     def addmaths(self, mathspassmarks = 35):
#         self.mathspassmarks = mathspassmarks
#         self.maths -= self.mathspassmarks

#     def addphysics(self):
#         self.physics -= self.physicspassmarks

#     def totalmarks(self):
#         return self.maths + self.physics
    
#     def showreports(self):
#         print(f"this is the current progress of {self.name}")
#         print(f"maths marks are {self.maths}")
#         print(f"physics marks are {self.physics}")
#         print(f"total marks are {self.totalmarks()}")

# student1 = Progressreport("sundeep", 85, 90)
# student1.addmaths()
# student1.addphysics()
# student1.showreports()


# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2*(self.length + self.width)

# trail1 = Rectangle(10,20)
# print(f"{trail1.area()}")
# print(f"{trail1.perimeter()}")

# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         self.balance -= amount

#     def showbalance(self):
#         print(f"current balance is : {self.balance}")
# customer1 = BankAccount(221234, 500)
# customer1.deposit(150)
# customer1.showbalance()
# customer1.withdraw(300)
# customer1.showbalance()

# class Car:
#     def __init__(self):
#         self.updateSoftware()
#     def drive(self):
#         print('driving')
#     def updateSoftware(self):
#         print('updating software')

# redcar = Car()
# redcar.drive()
# #redcar.__updateSoftware()


# class Car:
#     def __init__(self):
#         self.__max_speed = 200
#         self.name = "Super_car"

#     def drive(self):
#         print(f'max speed of a {self.name} is {self.__max_speed}')
# redcar = Car()
# redcar.drive()
# redcar.__max_speed = 10
# redcar.drive()
# print(redcar.__max_speed)


# #Aceesing private variables and methods in python
# class Car:
#     def __init__(self):
#         self.__max_speed = 200
#         self.name = "Super_car"
    
#     def drive(self):
#         print(f'max speed of a {self.name} is {self.__max_speed}')

#     def setmethod(self, speed):
#         self.__max_speed = speed

#     def __morefast(self):
#         print("speeding is illegal")
    
#     def accessprivatemethod(self):
#         self.__morefast()

# redcar = Car()
# redcar.drive()
# # redcar.__max_speed = 10
# redcar.setmethod(10)
# redcar.drive()
# redcar.accessprivatemethod()


# Method Overloadig Example

# class Human:
#     def sayHello(self, name = None):
#         # self.name = name
#         if name is not None:
#             print("hello " +name)
#         else:
#             print("Hello")

# obj1 = Human()
# obj1.sayHello()
# obj1.sayHello("Sundeep")



# Inheritance Example
# class User:
#     name = ""
#     def __init__(self, name = None, id = None):
#         self.name = name

#     def printname(self):
#         print(f'user name is {self.name}')

# class Student(User):
#     def __init__(self, id = None, name = None):
#         self.id = id
#         super().__init__(name)    
#     def printid(self):
#         print(f'student id is {self.id}')

# obj1 = User("sundeep")
# obj1.printname()

# obj2 = Student(2119)
# obj2.name = 'Kumar'
# obj2.printid()
# obj2.printname()

# class User:
#     def __init__(self, name):
#         self.name = name
#     def printname(self):
#         print(f'User name is {self.name}')
# class Programer(User):
#     def __init__(self, name):
#         # self.name = name
#         super().__init__(name)
#     def doPython(self):
#         print(f'user use python programing language')
# obj1 = User("sundeep")
# obj1.printname()

# obj2 = Programer("kumar")
# obj2.printname()
# obj2.doPython()


# # Nested Classes Example
# class Human:
#     def __init__(self, name):
#         self.name = name
#         self.head = self.Head(name)
#         self.legs = self.Legs(name)

#     class Head:
#         def __init__(self, name):
#             self.name = name
#         def think(self):
#             print(self.name +" Thinking")
#     class Legs:
#         def __init__(self, name):
#             self.name = name
#         def walk(self):
#             print(self.name +' Walking')

# person = Human("Sundeep")
# person.head.think()
# person.legs.walk()


# class Teacher:
#     def  __init__(self, name = None):
#         self.name = name
#     def teach(self):
#         print(f'Teacher {self.name} is teaching')
#     class Student:
#         def __init__(self, outer, name = None):
#             self.outer = outer
#             self.name = name
#         def learn(self):
#             print(f'Student {self.name} is learning from teacher {self.outer.name}')
        
# teacher = Teacher("Murali")
# teacher.teach()
# student = Teacher.Student(teacher, "Sundeep")
# student.learn()


class Teacher:
    def  __init__(self, name = None):
        self.name = name
    def teach(self):
        print(f'Teacher {self.name} is teaching')

class Professor:
    def __init__(self, name = None):
        self.name = name
    def teach(self):
        print(f'Professor {self.name} is teaching')

class Student:
    def __init__(self, outer, name = None):
        self.outer = outer
        self.name = name
    def learn(self):
        print(f'Student {self.name} is learning from teacher {self.outer.name}')
    
teacher = Teacher("Murali")
teacher.teach()
professor = Professor("Newton")
professor.teach()
student1 = Student(teacher, "Sundeep")
student1.learn()
student2 = Student(professor, "Mahi")
student2.learn()


