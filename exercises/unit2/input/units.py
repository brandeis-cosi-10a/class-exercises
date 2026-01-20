# write a function that converts from square feet to square meters
# then write a main method that prompts the user for a value in square feet,
# calls the conversion function, and prints out the result in square meters.
# 1 square foot is equivalent to 0.092903 square meters.

def sqft_to_sqm(sqft):
    return sqft * 0.092903

def main():
    sqft = float(input("Enter area in square feet: "))
    sqm = sqft_to_sqm(sqft)
    print(f"Area in square meters: {sqm}")

main()