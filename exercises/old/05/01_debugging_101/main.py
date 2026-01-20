def print_stuff():
    print("Hi this is a function")
    print("How do we get the debugger to here?")

x = input("Guess a lucky number: ")
print_stuff()
print(x, 7)  # <-- not a helpful debugging print
if x == 7:
    print("You win $1,000,000!")
else:
    print("Sorry, you lose")