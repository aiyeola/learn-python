temperature = 30

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")


if temperature == 30:
	print("An equal operator is used here")


name = "J"

if len(name) < 3:
	print("Name should have at least 3 characters")
elif len(name) > 50:
	print("Name shouldn't exceed 50 characters")
else:
	print("Name looks good")
