age = 22

if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"

print(message)

# Ternary operator
age = 22
message = "Eligible" if 18 <= age < 65 else "Not eligible"

print(message)
