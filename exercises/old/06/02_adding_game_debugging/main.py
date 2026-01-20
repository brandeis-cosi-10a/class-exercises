def prompt_and_check(solution):
    guess = input("Guess? ")
    
    if guess == solution:
        print("Correct! 1 point")
        return True
    else:
        print("BZZZT, wrong answer! The correct answer was: " + str(solution))
        return False    
    
prompt_and_check(34)