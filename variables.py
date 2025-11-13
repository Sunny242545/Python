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

s="sundeep"
#printing character at index 2
print(s[2])
#printing characters from 0-4
print(s[0:5])
#printing characters from last to first
print(s[::-1])
#printing characters from 2 to second last
print("characters from 2 to second last " +s[2:-2:-1])
#printing characters from last  to second last using length function
print("characters from last  to second last using length function " + s[len(s)-1:len(s)-3:-1])
#printing characters from last  to second last using negative indexing
print("characters from last  to second last " + s[-1:-3:-1])
#printing characters from 0 to second last with step 2
print("characters from 0 to second last with step 2 " + s[0:-1:2])