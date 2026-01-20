def main():
    var = 45
    print("Value of var in main:", var)
    ftn1()

def ftn1():
    var = -10
    ftn2()
    print("Value of var in ftn1:", var)

def ftn2():
    var = 99
    print("Value of var in ftn2:", var)

var = 100
main()
print("Value of var in global scope:", var)
