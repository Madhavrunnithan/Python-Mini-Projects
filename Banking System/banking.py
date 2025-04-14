class BankSystem:
    acc_id = 0000
    def __init__(self):
        self.acc_balance = 0
    def create_account(self,name):
        self.name = name
        self.acc_no = "IBA"+f"{BankSystem.acc_id:04d}"
        BankSystem.acc_id += 1
        self.pin = int(input("Create a 4 digit pin : "))
        print("Account created successfully")
        print("Account No : ",self.acc_no)
    
    def deposit(self):
        amount = float(input("Enter amount : "))
        pas = int(input("Pin : "))
        if pas == self.pin:
            self.acc_balance += amount
            print(f"{amount}Rs Deposited Successfully")
        else:
            print("Wrong pin")
        
    def withdraw(self):
        amount = float(input("Enter amount : "))
        pas = int(input("Pin : "))
        if pas == self.pin:
            if self.acc_balance >= amount:
                print(f"{amount}Rs withdraw successfully")
                self.acc_balance = self.acc_balance - amount
                print(f"balance : {self.acc_balance}Rs")
            else:
                print("Low Balance...Check your balance")
        else:
            print("Wrong pin")
    
    def view_balance(self):
        pas = int(input("Pin : "))
        if pas == self.pin:
            print(f"Account balance : {self.acc_balance}Rs")
        else:
            print("Wrong pin")

registered_users = dict()
i = 1
users = []
while(1):
    name = input("Enter name : ")
    if name not in registered_users.keys():
        print("No accounts found...!\nCreating account to enable services\n")
        user = BankSystem()
        user.create_account(name)
        registered_users.update({name:user})
        i+=1
        print("welcome , ",name)
    else:
        print(f"Welcome back , {name}")
    user1 = registered_users.get(name)
    ch = int(input(f"Account No : {user1.acc_no}\n1-withdraw\n2-deposit\n3-view balance\n4-exit\n"))
    
    if ch == 1:
        user1.withdraw()
    elif ch == 2:
        user1.deposit()
    elif ch == 3:
        user1.view_balance()
    elif ch == 4:
        break
    else:
        print("invalid")