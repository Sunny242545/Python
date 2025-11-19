list = []

for i in range(3):
    list.append([])
    for j in range(3):
        list[i].append(i+j)

print(list)
print(list[0][0])
print(list[1][2])

id = "xyz123"
password = "abc@123"
input_id = input("Enter your id: ")
if input_id == id:
    input_password = input("Enter your password: ")
    for i in range(3):
        if input_password == password:
            print("Login Successful")
            break
        else:
            print("Incorrect Password")
            if i < 2:
                input_password = input("Re-enter your password: ")
            else:
                print("Account Locked")
else:
    print("Invalid ID")

print("welcome to the guess my age game")
age = 25
exit_code = 999
guess = int(input("Guess my age: "))
while guess != exit_code:
    if guess < age:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Guess my age: "))