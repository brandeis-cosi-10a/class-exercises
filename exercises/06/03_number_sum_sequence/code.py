def ns_sequence(start, n):
    for i in range(n):
        digit_sum = 0
        for c in str(start):
            digit_sum += int(c)
        start = digit_sum * (i + 1)
    return start

def test_example1():
    assert ns_sequence(153, 0) == 153
    assert ns_sequence(153, 1) == 9
    assert ns_sequence(153, 2) == 18
    assert ns_sequence(153, 3) == 27
    assert ns_sequence(153, 4) == 36
    assert ns_sequence(153, 5) == 45

def test_example2():
    assert ns_sequence(2731, 0) == 2731
    assert ns_sequence(2731, 1) == 13
    assert ns_sequence(2731, 2) == 8
    assert ns_sequence(2731, 3) == 24
    assert ns_sequence(2731, 4) == 24
    assert ns_sequence(2731, 5) == 30
