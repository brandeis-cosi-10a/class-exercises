def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

def count_primes(start, stop):
    count = 0
    for i in range(start, stop + 1):
        if is_prime(i):
            count += 1
    return count


def test_example():
    assert count_primes(5, 11) == 3
    assert count_primes(0, 10) == 4
    assert count_primes(10, 2000) == 299