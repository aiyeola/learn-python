def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return 'FizzBuzz'
    if input % 3 == 0:
        return 'Fizz'
    if input % 5 == 0:
        return 'Buzz'
    return input


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(11))


#  Augmented assignment operator
a = 10
a //= 5
a %= 2
a += 1
print(a)
