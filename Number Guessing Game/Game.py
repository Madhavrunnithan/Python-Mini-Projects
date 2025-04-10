import pyttsx3
import random
import time

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

class Guessing_System: 
    #Class for the backend processing
    def __init__(self):
        self.number = 0
    def generate(self):
        self.number = random.randint(0,100)
        return self.number
    def process(self,num):
        diff = abs(self.number - num)
        if diff <= 5:
            engine.say("wow You are getting warmer")
            engine.runAndWait()
        elif(diff < 20):
            engine.say("You are getting warm")
            engine.runAndWait()
        elif( diff < 50):
            engine.say("You are getting cold")
            engine.runAndWait()
        else:
            engine.say("oh you are getting colder")
            engine.runAndWait()
    
class player:
    #Player class
    def __init__(self,name):
        self.name = name
        self.lastguess = 0

level = {1 : 10,2:5,3:3} #Level Dictionary

system = Guessing_System() 
while(1): #Main front end
    menu_input = int(input("Start Game(Press 1)\nExit Game(Press 2)\n"))
    if menu_input == 1:
        username = input("Username : ")
        user = player(username)
        while(1):
            lvl = int(input("Easy(Press 1) - 10 Tries\nMedium(Press 2) - 5 tries\nHard(Press 3) - 3 tries\n"))
            if lvl in level:
                max = level[lvl]
                break
            else:
                print("Enter valid level")
        system.generate()

        for i in range(max):    #Getting user input
            time.sleep(1)
            if(i > 0):
                print("Last Guess : ",user.lastguess)
            user_num = int(input("Guess a number : "))
            user.lastguess = user_num
            if user_num == system.number:
                engine.say("Wow You found it. You won the game , Congrats")
                engine.runAndWait()
                break
            else:
                system.process(user_num)
                print("try again")
                print("Remaining tries ",max - (i+1))
        engine.say("Game over\n")
        engine.runAndWait()

    elif menu_input == 2:
        print("Exiting...")
        break
    else:
        print("Enter valid input")
        continue
engine.stop()
        
