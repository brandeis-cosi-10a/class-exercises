def add(num1, num2):
    return num1 + num2

def test_add():
    assert add(1, 1) == 2
    assert add(3, 4) == 7


def count_letters(word):
    # This function returns the number of letters in a string. 
    # Numbers, spaces, and punctuation don't count toward the total.
    return len([x for x in word if x.isalpha()])

def test_count_no_spaces():
    assert count_letters("This") == 4

def test_count_with_spaces():
    assert count_letters("Spaces do not count") == 16

def test_count_with_numbers():
    assert count_letters("ab82fj1993A") == 5

def test_count_with_punct():
    assert count_letters("Spaces don't count") == 15

def test_count_with_symbols():
    assert count_letters("ab!@#") == 2

