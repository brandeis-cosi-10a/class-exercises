def multiplyPolynomials(p1, p2):
    result = [0] * (len(p1) + len(p2) - 1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            result[i + j] += p1[i] * p2[j]
    
    return result

def test_example():
    assert multiplyPolynomials([4, 0, 7, 5], [2, 5]) == [8, 20, 14, 45, 25]

def test_zeroes():
    assert multiplyPolynomials([2, 0, 0, 0, 0], [3, 0, 0, 0]) == [6, 0, 0, 0, 0, 0, 0, 0]

def test_constants():
    assert multiplyPolynomials([2], [3]) == [6]

def test_constant():
    assert multiplyPolynomials([2, 11, 2, -3], [6]) == [12, 66, 12, -18]
