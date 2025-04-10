import tkinter as tk
import re

class calculator:
    def __init__(self):
        self.sum = 0
        self.pos = 0
    
    def resetip(self):
        return input.delete(0,tk.END)
    
    def add(self):
        inp = input.get()
        input.insert(len(inp),"+")

    def sub(self):
        inp = input.get()
        input.insert(len(inp),"-")
    
    def mul(self):
        inp = input.get()
        input.insert(len(inp),"*")
    
    def div(self):
        inp = input.get()
        input.insert(len(inp),"/")

    def result(self):
        try:
            self.sum = eval(input.get())
            input.delete(0,tk.END)
            input.insert(0,f"{self.sum}")
        except:
            input.delete(0,tk.END)
            input.configure(validate="none")
            input.insert(0,"Invalid Expression")
            input.configure(validate="key")

    def is_valid(self,char):
        return re.match(r'^[0-9+*/.-]*$',char) is not None

cal = calculator()
    
root = tk.Tk()
root.title("Calculator App")
root.geometry("700x600")

top = tk.Frame(root)
top.pack()
bottom = tk.Frame(root)
bottom.pack()
foot = tk.Frame(root)
foot.pack()

vcmd = (root.register(cal.is_valid),"%P")

input = tk.Entry(top,width=15,font = ("Arial",50),validate="key",validatecommand=vcmd)
input.pack(pady=5)

addbut = tk.Button(bottom,text="+",font=("Arial",50),width=8,command=cal.add)
addbut.grid(row=1,column=0,padx=5,pady=5)

subbut = tk.Button(bottom,text="-",font=("Arial",50),width=8,command=cal.sub)
subbut.grid(row=1,column=1,padx=5,pady=5)

mulbut = tk.Button(bottom,text="*",font=("Arial",50),width=8,command=cal.mul)
mulbut.grid(row=2,column=0,padx=5,pady=5)

divbut = tk.Button(bottom,text="/",font=("Arial",50),width=8,command=cal.div)
divbut.grid(row=2,column=1,padx=5,pady=5)

eqbut = tk.Button(foot,text="=",font=("Arial",50),width=15,command=cal.result)
eqbut.pack(pady=5)

resetbut = tk.Button(foot,text="RESET",font=("Arial",30),width=8,command=cal.resetip)
resetbut.pack(pady=5)

root.mainloop()