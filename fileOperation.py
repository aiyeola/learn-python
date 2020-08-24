f = open('myfile.txt', 'r')
# firstline = f.readline()
# secondline = f.readline()
# print(firstline)
# print(secondline)
print(f.read())
f.close()


f = open('myfile.txt', 'r+')
for line in f:
    print(line, end="")

f.write("\nThis sentence will be appended.")
f.write("\nPython is Fun!")
f.close()
