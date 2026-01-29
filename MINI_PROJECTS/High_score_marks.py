# ----------------------------------------  QUIZ GAME PROJECT  ---------------------------------------------------------
file_name = "high_score.txt"
score = 0
high_score = 0
#load high score
def load_high_score():
    global high_score
    try:
        #open a file in read mode
        file = open(file_name,"r")
        high_score = int(file.read())
        file.close()
    except:
        pass

#save high score
def save_high_score():
    #open the file in write mode
    file = open(file_name,"w")
    file.write(str(high_score))
    file.close()


#PLAY QUIZ
def play_quiz():
    global score
    questions = ["what is the ouput of print(2-3)?", "Which Datatype stores true/false?", "Which Keyword is used to"
    "fetch global variable in the function?"]
    answers=["5","bool","global"] 
    for i in range(len(questions)):
        print("\nQ.",questions[i])
        user_answer = input("your answer: ")
        if user_answer == answers[i]:
            score=score+1
            print("Correct")
        else:
            print("wrong!!")


#MAIN PROGRAM
def main():
    #global allows updating same high score
    global high_score
    #load_previous_high_Score
    load_high_score() 
    #ask player the name   
    name = input("enter your name:")
    #start quiz
    play_quiz()
    #print final score
    print("\nQuiz over")
    print(name,"your high score is :", score)
    #compare score with high score
    if score>high_score:
        high_score=score
        save_high_score()
    else:
        print("high score is : ",high_score)

main()
