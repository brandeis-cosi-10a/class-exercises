def remove_evens_mutating(nums):
    for i in range(len(nums) - 1, -1, -1):
        if (nums[i] % 2) == 0:
            print("del")
            del nums[i]


def remove_evens_non_mutating(nums):
    new_nums = []
    for num in nums:
        if num % 2:
            new_nums.append(num)
    return new_nums


def test_mutating():
    n = [12, 1, 7, 2, 4, 5, 8]
    remove_evens_mutating(n)
    assert n == [1, 7, 5]


def test_mutating_all_evens():
    n = [2, 6, 4, 10, 100]
    remove_evens_mutating(n)
    assert n == []

def test_non_mutating():
    n = [12, 1, 7, 2, 4, 5, 8]
    result = remove_evens_non_mutating(n)
    assert result == [1, 7, 5]
    assert n == [12, 1, 7, 2, 4, 5, 8]

def test_non_mutating_all_evens():
    n = [2, 6, 4, 10, 100]
    result = remove_evens_non_mutating(n)
    assert result == []
    assert n == [2, 6, 4, 10, 100]
    