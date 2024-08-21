import math

def area(width, height):
    return width * height

def color(width):
    if width < 10:
        return "blue"
    elif width < 20:
        return "purple"
    else:
        return "red"

def diagonal_length(width, height):
    return math.sqrt(width**2 + height**2)

def rectangle_info(width, height):
    print("What a lovely rectangle!")
    print("It is " + str(height) + " high, and " + str(width) + " wide.")
    print("It has a delightful area of " + str(area(width, height)))
    print("It is a wonderful shade of " + str(color(width)))
    print("Its diagonal is " + str(diagonal_length(width, height)))

rectangle_info(10, 20)
rectangle_info(5, 100)
rectangle_info(25, 25)