print("Name?")
name = input()
print("Hello there, " + name)

print("How old are you (in years)?")
age = int(input())
print("You were probably born in the year " + str(2024 - age))

age_in_seconds = age * 365 * 24 * 60 * 60
print("You are approximately " + str(age_in_seconds) + " seconds old!")
