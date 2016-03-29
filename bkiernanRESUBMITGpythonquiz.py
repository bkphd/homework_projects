# Round 2: Graham: Thanks for your helpful comments.  Here are some notes for the re-sub.  I terminate the game now after the
# player scores four runs or misses the same question three times. I reduced the difficulty levels to three simply by
# chopping the "A" level from the instructions and a bit of editing on the Q: string numbers (curious or lucky players can
# still find the "secret" A level league). I reduced the line count in the game process (14), but I have to say that at some
# point the demand to reduce line count drives the "density" of process/ function calls so high that it becomes harder
# to read / decipher what's going on (my main criticism of that mad-libs code). Thoughts? Finally, I used the triple quotes and
# tried to be more specific with the descriptions.  I think that covers it.  Thanks again, I'm new to this so your comments are
# very very helpful, even stuff so simple you might not consider it


# Round 1 Note: I personalized this a bit in a couple of ways, but I think I meet the standards in the rubric. I made it into a
# question-answer "quiz" instead of having all the questions and all the answers on the screen at the same time.  That seemed
# a bit redundant to me. I also give players a study guide at the end with an answer key. I tried to have a bit of fun with
# the "game" part of it by building in some baseball aspects, including minor through major leagues for difficulty level, the
# three-strikes and you're out rule, and randomized taunting for wrong answers.

import random

#Lists

question_list = [                  "\n Q: For simple problems like 1 + 1, Python returns _____?",#1 questions (in theory,
                                                 "\n Q: For 2 - 1 * 8 + 1 Python returns _____?",#2   anyway) are progressively
                                                        "\n Q: For 17/2?, Python returns _____?",#3     more difficlut
         "\n Q: How does adding a decimal effect the answer? For 17/2.0?, Python returns _____?",#4
                                     "\n Q1: In Python spacing, or _____tation, really matters!",#5
             "\n Q2: Python name is related to the comedy troupe: _____ Python's Flying Circus.",#6
        "\n Q3:Complete the following Python lyric: spam, spam, spam, spam, spam, spam,  _____!",#7
    "\n Q4: What is the index number for the value nee in l = [\"x\", \"nee\", \"spam\"] _____?",#8
                                    "\n Q5: What does Python return for \"ABC\" + \" D\" _____?",#9
                                                        "\n Q6: Beautiful is better than _____?",#10
             "\n Q7: Given list a = [23, 7, 10, 2], what is the value returned by len(a) _____?",#11
                     "\n Q8: Python uses logical operators too. For (1>0) Python returns _____?",#12
            "\n Q9: The _____ statement is used during de-bugging to check expected conditions.",#13
               "\n Q10: What character will cause an error in the statement: If (1 > 0): _____?",#14
                                                     "\n Q11: Type the equality operator _____?",#15
                                "\n Q12: Line feed is achieved by the character sequence _____.",]#16

answer_list =[              "2",#1
                            "9",#2
                            "8",#3
                          "8.5",#4
                        "inden",#5
                        "Monty",#6
                         "spam",#7
                            "1",#8
                        "ABC D",#9
                         "ugly",#10                   
                            "4",#11
                         "TRUE",#12
                       "assert",#13                  
                            "I",#14
                           "==",#15
                          "\\n",]#16                  

league_list = ["a","A", "aa", "AA", "aaa","AAA", "mlb", "MLB"] #removes capitalization as an issue

q_level_list = [0,0,4,4,8,8,12,12] #degree of difficulty for each league entry possibility


taunt_list = [
                                                              "\n Can't hit a curveball?",
                                                  "\n Got caught lookin' for a fastball!",
                                                           "\n Open your eyes next time!",
                                                          "\n It's a long bus ride home!",                         
                                                          "\n Go back to Little League!!"]
#Variables

user_input_league = " "
user_input_answer = " "
formatted_answer = ""
swapped_str = ""
sum_txt = ""

score = 0
misses = 0
q_level = 0
tries = 0

#############################################################################
def pick_league(user_input_league, league_list, q_level, q_level_list, tries):
    '''Player uses the raw_input function to select a degree of difficulty in the
    game.  Degree of diffculty id returned as q_level from a list that has the same
    index structure as the allowable league entries.  A oop here is icluded to account
    for typos and input mistakes'''
    user_input_league = raw_input("Type a league and hit enter: ")

    if user_input_league in league_list:
        print "\n Welcome!"
        q_level = q_level_list[league_list.index(user_input_league)]
        return q_level

    elif user_input_league not in league_list: #allows for typos and other mistakes
        while tries < 2:                       #1+2=3 strikes and you're out
            print "Try again. \n"
            user_input_league = raw_input("Type a league and hit enter: ")
            tries = tries + 1
            if user_input_league in league_list:
                print "\n Welcome!"
                q_level = q_level_list[league_list.index(user_input_league)] 
                return q_level

#############################################################################
def swap_answer(answer_list, q_level, swapped_str, question_list):
    '''This process takes the correct answer for the question and formats it for
    entry into the answer string.  The formatted answer is swapped with the blank
    in the quesion and punctuation is corrected.  The output is the correctly
    answered question formatted into a statement and added to a list of its kind'''

    formatted_answer = ("__" + answer_list[q_level] + "__")

    swapped_str = (swapped_str + question_list[q_level])

    edited_question = swapped_str.replace("_____", formatted_answer)

    edited_question = edited_question.replace("?",".")

    return edited_question
#############################################################################
def study_questions(question_list, q_level, answer_list):
    '''This process prints the study guide for questions missed or not seen'''
    for q in question_list[q_level+1:]:
        print q
    print "\n The answer key for missed / unasked questions: \n"
    for a in answer_list[q_level:]:
        q_level = q_level + 1
        print "A:", q_level, "is ", a
    raise SystemExit
        
#############################################################################
def end_game(score, sum_txt, question_list, q_level, misses):
    '''Monitors the score and misses and terminates after four correct answers or
    three strikes on the same question. The output is a summary of the game and a
    printed study guide'''
    if(score==4):
        print "\n" * 50, "Great job, slugger! Your final score: ", score
        print "Questions you answered correctly: \n", sum_txt
        print "\n The pitches you never saw:" # creates study guide
        study_questions(question_list, q_level, answer_list)       
    if(misses == 3):
        print "\n" * 50, "Three strikes and you're out! Your final score: ", score
        print "Questions you answered correctly: \n", sum_txt
        print "\n The pitch you struck out on: \n", question_list[q_level]
        print "\n The pitches you never saw:" # creates study guide
        study_questions(question_list, q_level, answer_list)

#############################################################################
def set_screen():
    '''This process takes no inputs and prints some simple outputs to set up the screen
    for the game'''
    print "\n" * 10
    print "Want to play Python's Big League Baseball Challenge?"
    print "\n Enter a league for level of difficulty: AA (easy), AAA (medium), MLB (hard) \n"
    return None

############################################################################
def ask_question(misses, sum_txt, question_list, q_level):
    '''This process monitors misses, clears the screen to make things visually easier
    for the player, and then prints the next question indexed by league choice / degree
    of difficult'''
    if (misses == 0):
        print "\n" * 50, sum_txt, "\n" *23            
    print question_list[q_level]

###########################################################################
def python_baseball(q_level, misses, sum_txt, question_list, user_input_answer, answer_list, score):
    '''This process calls other the other functions and runs the game.'''
    set_screen()
    q_level = pick_league(user_input_league, league_list, q_level, q_level_list, tries)# calls pick_league
    while (q_level < 16):
        ask_question(misses, sum_txt, question_list, q_level)
        user_input_answer = raw_input("\n Type your answer, be exact, hit enter. ")# uses raw_input          
        if (user_input_answer == answer_list[q_level]):
            misses = 0
            sum_txt = sum_txt + (swap_answer(answer_list, q_level, swapped_str, question_list))# calls swap_answer            
            score=(score + 1)
            end_game(score, sum_txt, question_list, q_level, misses) # calls end_game for winners                
            q_level = q_level + 1
        elif(user_input_answer != answer_list[q_level]):                
            print "\n" * 50, "\n Boo! ", taunt_list[random.randrange(0,4)]
            misses = misses + 1
            end_game(score, sum_txt, question_list, q_level, misses)# calls end_game for losers
print python_baseball(q_level, misses, sum_txt, question_list, user_input_answer, answer_list, score)
