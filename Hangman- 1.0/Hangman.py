import random
import sys
user = input("Do you want to play music(y/n)?")
if user == "yes":
        import os
        os.startfile('HangmanMusic.mp3')

elif user == "no":
        print("Ok! Starting game!")

words=[
"War","Brother","Winter"
,"Sneeze","Word"
,"Agreement"
,"Theory"
,"Slope"
,"Need"
,"Event"
,"Help"
,"Play"
,"Price"
,"Birth"
,"Respect"
,"Month"
,"Move"
,"Use"
,"Produce"
,"Substance"
,"Scale"
,"Letter"
,"Oil"
,"Meeting"
,"Size"
,"Death"
,"Servant"
,"Driving"
,"Hope"
,"Room"
,"Invention"
,"Shake"
,"Nation"
,"Relation"
,"Love"
,"Tin"
,"River"
,"Summer"
,"Weight"
,"Increase"
,"Crack"
,"Flower"
,"Base"
,"Offer"
,"Mountain"
,"Committee"
,"Ray"
,"Blood"
,"Rain"
,"Name"
,"Amount"
,"Woman"
,"Paper"
,"Trade"
,"Money"
,"Wind"
,"Friend"
,"Teaching"
,"Group"
,"Story"
,"Judge"
,"Science"
,"Comparison"
,"Religion"
,"Paint"
,"Harbor"
,"Man"
,"Request"
,"Answer"
,"Meal"
,"Vessel"
,"Swim"
,"Reading"
,"Knowledge"
,"Machine"
,"Amusement"
,"Digestion"
,"List"
,"Snow"
,"Current"
,"Stitch"
,"Sand"
,"Smell"
,"Company"
,"Family"
,"Reaction"
,"Shock"
,"Owner"
,"Lift"
,"Cotton"
,"Fear"
,"Steam"
,"Observation"
,"Animal"
,"Attempt"
,"Butter"
,"Music"
,"Rest"
,"Unit"
,"Desire"
,"Representative"
,"Sugar",
"Market",
"Wood",
"Front",
"Top",
"Idea",
"Art",
"Thunder",
"Value","Grass"


]
a=0
while a==0:
    Rightword=random.choice(words)
    correctword=Rightword.lower()
    correctletters=set(list(correctword))
    guessed=[]
    print("Welcome to Damon YT's Hangman!")
    print("#You will get *number of letters in word* + 5 chances to guess.")
    print("#Incase you notice the missing Hangman, I oppose Capital Punishment ;)")
    print("1. Start")
    print("2. Quit")
    b=input("Your choice: ")
    if b=="2":
       print("Thanks for playing")
       sys.exit()
    if b=="1":
        print("Guess this word: ")
        dashes=("_ "*len(correctword))
        print(dashes)
        c=1
        while c< (len(correctword)+6):
            letter=input("Your Guess: ")
            if letter==("CheatCode"):
                print("YOU WIN")
                print("The word is", correctword)
                break
            if letter in correctword and letter not in guessed and len(letter)==1:
                guessed.append(letter)
                print("Yes.You got that right")
            else:
                print("Nope, wrong letter. Try again.")
            for letter in correctword:
                if letter in guessed:
                    print(letter,end=" ")
                else:
                    print("_ ",end=" ")
            print()
            print("You have ", len(correctword)+5-c, "tries remaining.")
            c+=1
            if len(guessed)==len(correctletters):
                print("Congratulations!!!")
                print("You have guessed wisely! ")
                print(correctword,"is the word you have correctly guessed.")
                print()
                c+=30
                break
            if c==(len(correctword)+6):
                print("The correct word is", correctword)
                print("You got " ,guessed,"correct.")
                print("Unlucky my friend.")
                print("Another go?.")
                print()
