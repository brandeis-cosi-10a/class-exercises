
# define function
def ns_sequence(start, n):
    lastNum = start
    all_nums = ''

    # for loop over 'n' - the number of digits
    for i in range(n):
        sum = 0
        # for loop over every character in the number
        for c in str(lastNum):
            # keep a running sum of the digits
            sum += int(c)
        
        # multiply by the number of numbers generated so far
        sum *= i + 1
        lastNum = sum
        all_nums += '\t' + str(lastNum)

    # return the last number
    return int(lastNum)

if __name__ == "__main__":
    start = int(input("Give me a starting number: "))
    num = int(input("How many numbers should I generate? "))

    print(ns_sequence(start, num))

def test_example():
    assert ns_sequence(153, 5) == 45

def test_example2():
    assert ns_sequence(2731, 5) == 30

