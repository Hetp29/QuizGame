def new_game():
    guesses = [] 
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print("------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)
        
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)
def check_answer(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else: 
        print("Wrong")
        return 0
    
def display_score(correctGuesses, guesses):
    print("----------------------")
    print("results")
    print("----------------------")
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end="")
    print()
    
    score = int((correctGuesses / len(questions)) * 100)
    print("your score is: " + str(score)+"%")
    
def play_again():
    respond = input("Do you want to play again?: (yes or no): ")
    respond = respond.upper()
    if respond == "YES":
        return True
    else:
        return False

#create dictiomary, or collection to hold questions and answers we have
#create dictionary titled "questions"
questions = {
    "Where was Lord Krishna born?: ": "B",
    "Where does Lord Shiva and his family live?: ": "D",
    "Finish this: Bramha, Vishnu, _______... ": "A",
    "Which pandav killed Bishma Pitama in Mahabharata? ": "C"
}
#if you did multiple choice, you could use a 2D list/array to store the options 
options = [["A. Vrindhavan", "B. Mathura", "C. Gokul", "D. Lanka"],
        ["A. Mount Everest", "B. Ayodhya", "C. Lanka", "D. Mount Kailesh"],
        ["A. Mahesh", "B. Krishna", "C. Ram", "D. Ganesh"],
        ["A. Bheem", "B. Yudishtir", "C. Arjun", "D. Nakul"]]

new_game()
while play_again():
    new_game()
print("Have a good one")