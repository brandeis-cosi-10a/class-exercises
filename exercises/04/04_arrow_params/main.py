def arrow(shaft_length=15, head_height=5, fill='*', hollow=False):
    '''
    Print an arrow shape.
    `shaft_length` is an integer controlling how long the arrow shaft is
    `head_height` is an integer controlling how tall the arrowhead is. The arrowhead will be (head_height*2)+1 rows tall.
    `fill` is the character used to draw the arrow
    `hollow` is a boolean determining whether the arrow head is drawn hollowly or filled in
    '''
    for i in range(head_height):
        print_head_row(shaft_length, i, fill, hollow)

    print(fill * (shaft_length + 1) + get_fill(fill, hollow) * (head_height - 1) + fill)

    for i in range(head_height-1, -1, -1):
        print_head_row(shaft_length, i, fill, hollow)

def get_fill(fill_char, hollow):
    '''Returns fill_char if hollow is False, space otherwise'''
    if hollow:
        return " "
    return fill_char

def print_head_row(shaft_length, head_width, fill, hollow):
    '''Prints a single row of the arrow head'''
    print(" " * shaft_length + fill, end='')
    if head_width == 0:
        print()
    else:
        print(get_fill(fill, hollow) * (head_width - 1)+ fill) 

arrow(10, 3, "$", True)
arrow(head_height=5)
arrow(head_height=7, hollow=True)