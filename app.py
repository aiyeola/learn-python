# price = 10
# price = 20.44
# name = 'Victor'
# checked = True
# is_published = False
# print(price)


# name = input('What is your name? ')
# print('Hi ' + name)

# from ecommerce.shipping import calc_shipping

# calc_shipping()

from pathlib import Path

# path = Path("ecommerce1")

# print(path.rmdir())


path = Path()
for file in path.glob('*'):
    print(file)
