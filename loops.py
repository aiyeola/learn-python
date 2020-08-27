# i = 1

# while i <= 5:
#     print(i)
#     i += 1
# print("Done")

# # For loop
# for item in ['Mosh', 'John', 'Sarah']:
#     print(item)

# # Nested loop
# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")

users = {
    'Ade': 'active',
    'Daniel': 'inactive',
    'Adele': 'inactive'
}


users_dict = users.items()
print(users_dict)

for index, status in enumerate(users):
    print(index, status)

for user in users.keys():
    for status in users.values():
        print(user, status)

#  looping through a sequence of numbers
for digit in range(0, 100, 10):
    print(digit)


counter = 5
while counter > 0:
    print("Counter = ", counter)
    counter = counter - 1


# break terminates the loop
j = 0
for i in range(5):
    j = j + 2
    print('i = ', i,
          'j = ', j)
    if j == 6:
        break

# continue is used to skip a value in the loop
j = 0
for i in range(5):
    j = j + 2
    print('i= ', i, 'j= ', j)
    if j == 6:
        continue
    print("I will be skipped over if j=6")


# try ... expect controls how the program proceeds when an error occurs

# try:
#     answer = 12 / 0
#     print(answer)
# except:
#     print('An error occurred')

# try:
#     userInput1 = int(input("Please enter a number: "))
#     userInput2 = int(input("Please enter another number: "))
#     answer = userInput1/userInput2
#     print("The answer is ", answer)
#     myFile = open("missing.txt", 'r')
# except ValueError:
#         print("Error: You did not enter a number")
# except ZeroDivisionError:
#         print("Error: Cannot divide by zero")
# except Exception as e:
#         print("Unknown error: ", e)
