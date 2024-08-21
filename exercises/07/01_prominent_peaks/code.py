def find_most_prominent(peaks):
    max_index = None
    max_prom = None

    if len(peaks) == 0:
        return (None, None)
    if len(peaks) == 1:
        return (peaks[0], 0)
    
    for i in range(len(peaks)):
        prom = peaks[i]
        if i == 0 and len(peaks) > 1:
            prom = peaks[i] - peaks[i + 1]
        if i == len(peaks)-1 and len(peaks) > 1:
            prom = peaks[i] - peaks[i - 1]
        if i > 0 and i < (len(peaks) - 1):
            prom = min(peaks[i] - peaks[i - 1], peaks[i] - peaks[i + 1])

        if (max_prom is None) or (prom > max_prom):
            max_index = i
            max_prom = prom
    return max_prom, max_index

def test_example1():
    assert find_most_prominent([1, 7, 8, 3, 10, 4, 5]) == (6, 4)


def test_example2():
    assert find_most_prominent([10, 20, 15, 1, 8, 2, 4]) == (6, 4)

def test_example3():
    assert find_most_prominent([10, 3, 13, 11, 5, 1]) == (7, 0)

def test_edges():
    assert find_most_prominent([]) == (None, None)
    assert find_most_prominent([1]) == (1, 0)
    assert find_most_prominent([1, 2]) == (1, 1)
    assert find_most_prominent([1, 2, 4]) == (2, 2)

def test_tie():
    assert find_most_prominent([4, 2, 5, 3]) == (2, 0)
