import math

# calculates the area of the circle  
def circle_area(r):
    return math.pi * r * r

# Keep asking for input until a valid value is given
while True:
    try:
        r = float(input("Enter the radius of the circle: "))
        if r <0:
            print("Please enter a positive number")
            continue        
        break
    except ValueError:
        print("Invalid input. Please enter a number")

print("Area of the circle is ", circle_area(r))