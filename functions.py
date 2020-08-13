# Functions
# Positional argument
def greet_user(name):
    print(f"Hi {name}")
    print("Hope you're having a solid day? ")


print("Start")
greet_user("John")
print("Finish")

# Keyword arguments
#  They increase the readability of your code with draw back of being
#  verbose and ignoring order


def cost(initial_cost, discount, interest):
    return initial_cost * discount * interest


ans = cost(initial_cost=40, discount=2, interest=0.4)
print(ans)
