# Rectangle info

## Part 1

Write a few functions:
1. `area(width, height)` which takes the width and height of a rectangle as a parameter, and returns the area (`width * height`) of the rectangle.
2. `color(width)` which takes the width of a rectangle as a parameter, and returns different colors for different ranges (e.g. "blue" for widths less than 10, "purple" for widths between 10 and 20, "red" for widths greater than 20).
3. `diagonal_length(width, height)` which takes in the width and height of a rectangle as parameters, and returns the length of the diagonal: the square root of ((width squared) + (height squared)).
    * Note: to perform a square root, add `import math` as the first line of your program, then use the function `math.sqrt(<number>)`,
    * e.g. `math.sqrt(9)` would evaluate to `3`

## Part 2

Write a function, `rectangle_info(width, height)` which prints out the height, width, area, color, 
and diagonal length of the rectangle, using the 3 functions defined in part 1.