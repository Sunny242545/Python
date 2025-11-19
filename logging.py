#logging Example with Fibanacci custom iterator
# import logging

# logging.basicConfig(filename = "variables.log", level = logging.INFO, format= "%(asctime)s,%(message)s")

# class FibanacciNum():
#     def __init__(self, max_value):
#         self.max_value = max_value
#         self.current = 0
#         self.next = 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current<self.max_value:
#             fibnum = self.current
#             self.current = self.next
#             self.next = fibnum+self.next
#             logging.info("fibnum : {} current : {} next : {}".format(fibnum, self.current, self.next))
#             return fibnum
#         else:
#             raise StopIteration
        
# for i in FibanacciNum(10):
#     print(i)
