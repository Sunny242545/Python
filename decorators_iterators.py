 #Decorators

# #Iterator Example

# class CountNumber:
#     def __init__(self, max_val):
#         self.max_val = max_val
#         self.count = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.count < self.max_val:
#             self.count +=1
#             return self.count
#         else:
#             raise StopIteration
# for i in CountNumber(10):
#     print(i)

# # generators
# def CountGenerator(val):
#     current =0
#     while current < val:
#         yield current
#         current +=1
# for i in CountGenerator(10):
#     print(i)

# #Decorator example
# def decorator(func):
#     def wrapper():
#         print("this code executed before job function")
#         return func()
#     return wrapper

# @decorator
# def job():
#     print("this is my job function")

# job()