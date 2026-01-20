# write a function that says hello to a user by name
# then write a main method that prompts the user for their name,
# calls the hello function, and prints out the result.

def say_hello(name):
    return "Hello, " + name + "!"

def main():
    user_name = input("Enter your name: ")
    greeting = say_hello(user_name)
    print(greeting)

main()
