for i in range(60, 71):
    print(str(i) + " divided by 3 is " + str(i / 3))
    if i == 64:
        print(str(i) + " is a perfect square!")
    else:
        print(str(i) + " is not a perfect square")

for i in range(10):
    num = int(input("Enter a number: "))
    if num < 0: 
        print("Be a little more positive!")
    else:
        print(str(num) + " is a great number!")