a, b = 0, 1
while a < 10:
    # print(a)
    a, b = b, a+b

course = 'Python is interesting'
another = course[:]

print(another)

first = 'John'
last = 'Smith'

message = first + ' [' + last + '] is a coder'
# Formatted string
msg = f'{first} [{last}] is a coder'
print(msg)

print('Python' in course)
