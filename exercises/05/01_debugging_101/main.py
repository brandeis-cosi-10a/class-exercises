x = input("Guess a lucky number: ")
print(x, 7)  # <-- not a helpful debugging print
if x == 7:
    print("You win $1,000,000!")
else:
    print("Sorry, you lose")