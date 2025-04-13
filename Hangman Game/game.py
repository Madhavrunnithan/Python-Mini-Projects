import random

class Gamesystem:
    def __init__(self):
        self.word_list = [
            "pirate", "castle", "dragon", "wizard", "unicorn",
            "banana", "monster", "cookie", "spaceship", "zombie",
            "treasure", "puzzle", "robot", "island", "rocket",
            "pumpkin", "magic", "jungle", "bubbles", "ghost"
        ]
        self.life = 6

    def wordselecter(self):
        self.word2 = ""
        index = random.randint(0,19)
        self.word = self.word_list[index]
        for i in range(len(self.word)):
            self.word2 += "_"
    
    def checker(self,ch):
        flag = 0
        for i in range(len(self.word)):
            if self.word2[i] == "_" and self.word[i] == ch:
                self.word2 = self.word2[0:i] + ch + self.word2[i+1:]
                flag = 1
        if flag == 0:
            self.life = self.life - 1
            print("Wrong letter")
            return self.printstatus()
        else:
            return self.printstatus()
        
    def printstatus(self):
        if "_" not in self.word2:
            print("Congrats....! You WON")
            print("word : ",self.word2)
            return 1
        elif self.life == 0:
            print("You have FAILED")
            print("Actual word : ",self.word)
            return -1
        else:
            print("word : ",self.word2)
            print("Life remaining : ",self.life)
            return 0

        


system = Gamesystem()
while(1):
    ip = int(input("1-Start Game\n2-Exit\n"))
    if ip == 1:
        system.wordselecter()
        ret = system.printstatus()
        while(1):
            ch = input("Guess a letter   : ")
            ret = system.checker(ch)
            if ret == -1 or ret == 1:
                break
    elif ip == 2:
        print("exiting.....")
        break
    else:
        print("Invalid")