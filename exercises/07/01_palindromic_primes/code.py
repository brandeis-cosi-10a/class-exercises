def is_prime(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True

def is_palindrome(num):
    num_str = str(num)
    for i in range(len(num_str)):
        if num_str[i] != num_str[-i-1]:
            return False
    return True

def find_nth_palprime(n):
    curr = 2
    found = 0
    while True:
        if is_palindrome(curr) and is_prime(curr):
            if found == n:
                return curr
            found += 1
        curr += 1

def test_is_prime():
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(7)
    assert is_prime(101)
    assert not is_prime(4)
    assert not is_prime(10)
    assert not is_prime(49)

def test_is_palindrome():
    assert is_palindrome(101)
    assert is_palindrome(3)
    assert is_palindrome(404)
    assert is_palindrome(44)
    assert is_palindrome(331242133)

def test_nth_palprime():
    assert find_nth_palprime(0) == 2
    assert find_nth_palprime(1) == 3
    assert find_nth_palprime(2) == 5
    assert find_nth_palprime(4) == 11
    assert find_nth_palprime(5) == 101
    assert find_nth_palprime(6) == 131
    assert find_nth_palprime(20) == 10301
    assert find_nth_palprime(100) == 94349