#Declaration of the score Variable

score = 0
# Function which increases the score variable by 1 each time the user gets the correct answer
def correct():
    global score
    score+=1
# main function for the game, includes the rules
def main():
    print("Welcome to a history trivia quiz !. There will be a total of 10 questions. Try and see how many you can get right!\n")
    print("On screen, there will be a question, with 4 possible choices. Type out the letter which correspons to the correct answer!\n")
    print("At the end of the game, your score will be displayed, as well as the time it took you to do the quiz. Good luck !\n")
    
   

# Function which allows the user to input the answer to the question
def response():
    response = input("Please type the letter corresponding to your answer: ")
    global user_answer
    user_answer = response.upper()
# Question 1
def q1():
    print("Question 1. Which of the following countries allied with Germany in WW1 ?")
    print("A. Russia")
    print("B. Serbia")
    print("C. USA")
    print("D. Ottoman Empire")
    response()
    if user_answer == "D" :
        print("Correct, great job !\n")
        correct()
    else:
        print("Nice try, but that is incorrect. The correct answer is the Ottoman Empire !\n")
# Displays the users score after each question
def display_score():
    print("You have correctly answered " + str(score) + " questions correctly so far !\n")
# Question 2
def q2():
    display_score()
    print("What was the name of the peace treaty signed to mark the end of the first World War ?")
    print("A. Treaty of Naples")
    print("B. Treaty of Asiago")
    print("C. Treaty of Somme")
    print("D. Treaty of Versailles")
    response()
    if user_answer.upper() == 'D':
        print("Correct, great job !\n")
        correct()
    else:
        print("Nice try, but that is incorrect. The correct answer is the Treaty of Versailles !\n")
# Question 3
def q3():
    display_score()
    print("What was the name of the German AirForce in WW2\n")
    print("A. The Panzers")
    print("B. The Dessert Rats")
    print("C. The Lufftwaffe")
    print("D. The Third Reich")
    response()
    if user_answer.upper() == 'C':
        print("Correct, great job !\n")
        correct()
    else:
        print("Nice try, but that is incorrect. The correct answer is the Luftwaffe !\n")
# Question 4
def q4():
    display_score()
    print("What country did Napoleon try and invade, but failed ?")
    print("A. Russia")
    print("B. India")
    print("C. USA")
    print("D. China")
    response()
    if user_answer.upper() == 'A':
        print("Correct, great job !\n")
        correct()
    else:
        print("Nice try, but that is incorrect. The correct answer is Russia !\n")
# Question 5
def q5():
    display_score()
    print("What is the name if the first American President")
    print("A. Thomas Jefferson")
    print("B. George Washington")
    print("C. Thomas Edison")
    print("D. Woodrow Wilson")
    response()
    if user_answer.upper() == 'B':
        print("Correct, great job !\n")
        correct()
    else:
        print("Nice try, but that is incorrect. The correct answer is George Washington !\n")


def q6():
    display_score()
    print("Which British official tried to broker a peace deal with Hitler")
    print("A. Winston Churchill")
    print("B. King Goerge V")
    print("C. Neville Chamberlain")
    print("D. Queen Victoria")
    response()
    if user_answer.upper() == 'C':
        print("Correct, great job !\n")
        correct()
    else:
        print("Nice try, but that is incorrect. The correct answer is Neville Chamberlain!\n")
def q7():
    display_score()
    print("Which official whose assanitation resulted in the commencement of WW1 ?")
    print("A. Tsar Nicolas")
    print("B. Archduke Franz Ferdinand")
    print("C. Emperor Kaiser Wilhem II")
    print("D. Woodrow Wilson")
    response()
    if user_answer.upper() == 'B':
        print("Correct, great job !\n")
        correct()
    else:
        print("Nice try, but that is incorrect. The correct answer is Archduke Franz Ferdinand  !\n")

def q8():
    display_score()
    print("Who was the lader of the confederates during the American Civil War ?")
    print("A. Jefferson Davis")
    print("B. Robert E Lee")
    print("C. General Grant")
    print("D. Abraham Lincoln")
    response()
    if user_answer.upper() == 'A':
        print("Correct, great job !\n")
        correct()
    else:
        print("Nice try, but that is incorrect. The correct answer is Jefferson Davis !\n")

def q9():
    display_score()
    print("What leader pulled Russia out of the first world war ?")
    print("A. Tsar Nicolas")
    print("B. Tsar Alexander")
    print("C. Vladamir Lenin")
    print("D. Joseph Stalin")
    response()
    if user_answer.upper() == 'C':
        print("Correct, great job !\n")
        correct()
    else:
        print("Nice try, but that is incorrect. The correct answer is Vladamir Lenin !\n")

def q10():
    display_score()
    print("What was the name of the pact including Eastern Block nations in after WW2 ?")
    print("A. Axis Pact")
    print("B. NATO")
    print("C. Tripartie Pact")
    print("D. The Warsaw Pact")
    response()
    if user_answer.upper() == 'D':
        print("Correct, great job !\n")
        correct()
    else:
        print("Nice try, but that is incorrect. The correct answer is the Warsaw Pact !\n")


    

    

# Main Game Loop

while True:
    score = 0
    main()
    q1()
    q2()
    q3()
    q4()
    q5()
    q6()
    q7()
    q8()
    q9()
    q10()
    print("You got " + str(score) + " questions corrctly, out of 10 questions !\n")
    global answer
    answer = input("Would you like to play again ? Please say either yes or no: \n")
    if answer.upper() == "NO":
        print("Thank you for playing!")
        break
    
          
        
    
    
