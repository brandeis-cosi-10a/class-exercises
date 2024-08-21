print("Welcome to the geography quiz!")
incorrect = 0
points = 0

def do_question(number, question, expected_answer):
    global points
    global incorrect
    if incorrect >= 2:
        return
    
    answer = input("Question " + str(number) + ": " + question)
    if answer == expected_answer:
        print("Correct!")
        points = points + 1
    else:
        print("Incorrect! The answer was '" + expected_answer + "'")
        incorrect = incorrect + 1
        
do_question(1, "Does Kansas border Colorado? (y/n) ", "y")
do_question(2, "How many countries are in Europe? ", "50")
do_question(3, "In which state can you find the Grand Canyon? ", "Arizona")
do_question(4, "Which North American city has a larger population: Los Angeles or Mexico City? ", "Mexico City")
do_question(5, "Which country has the most volcanoes? ", "Indonesia")
print("You earned " + str(points) + " points!")