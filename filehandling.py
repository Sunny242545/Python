#reading the file in python without pandas

# data = open("path", "r")
# content = data.readlines()
# for i in content:
#     print(i, end = '')

# with open("path") as f:
#     lines = f.readlines()
#     for i in lines:
#         print(i, end ='')

# import os.path

# filepath = "sample.txt"

# if not os.path.isfile(filepath):
#     print("file does not exist")
# else:
#     with open(filepath, 'a+') as file:
#         file.write("\n I love Mahi ")
#         file.seek(0) #with a+ mode my file pointer is at the end of the file so to read the file we need to set the pointer to the begining of the file
#         lines = file.readlines()
#         for i in lines:
#             print(i, end= '')