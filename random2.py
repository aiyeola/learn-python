import random

for i in range(3):
    print(random.random())
    print(random.randint(10, 20))


names = ['John', 'Mosh', 'Victor', 'Tedd']
leader = random.choice(names)
print(leader)
