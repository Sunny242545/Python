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

# Nested Classes Example without using inner class

# class Teacher:
#     def  __init__(self, name = None):
#         self.name = name
#     def teach(self):
#         print(f'Teacher {self.name} is teaching')

# class Professor:
#     def __init__(self, name = None):
#         self.name = name
#     def teach(self):
#         print(f'Professor {self.name} is teaching')

# class Student:
#     def __init__(self, outer, name = None):
#         self.outer = outer
#         self.name = name
#     def learn(self):
#         print(f'Student {self.name} is learning from teacher {self.outer.name}')
    
# teacher = Teacher("Murali")
# teacher.teach()
# professor = Professor("Newton")
# professor.teach()
# student1 = Student(teacher, "Sundeep")
# student1.learn()
# student2 = Student(professor, "Mahi")
# student2.learn()