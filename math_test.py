import math

# Prints all entities of math module
print(dir(math))

# Rounds up the integer
print(math.ceil(5.6))  # prints 6

# Rounds down to nearest integer
print(math.floor(5.6))  # prints 5

# Discards the decimal portion of number
print(math.trunc(5.6))  # prints 5

# Raises a base number to the power of an exponent(returns float)
print(math.pow(5,6))   # 5^6 = 15625.0

#Euclidean distance - for 2D -hypotenuse of a right traingle
print(math.hypot(5,6)) #  √(5² + 6²) = 7