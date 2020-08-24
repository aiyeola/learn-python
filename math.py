import math

number = math.ceil(2.9)
number2 = math.floor(2.9)
print(number)
print(number2)

# i = i+1
# submitted += 1
# x = x * 2 - 1
# hypot2 = x * x + y * y
# c = (a + b) * (a - b)


#  Function Annotations
def munge(input: AnyStr):
    return None


def munge() -> AnyStr:
    return None


def munge(sep: AnyStr = None):
    return None


def munge(input: AnyStr, sep: AnyStr = None, limit=1000):
    return None


FILES = ['setup.cfg',
         'tox.ini', ]
initialize(FILES,
           error=True,)

FILES = [
    'setup.cfg',
    'tox.ini',
]
initialize(FILES,
           error=True,
           )
