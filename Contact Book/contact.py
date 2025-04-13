class ContactBook:
    def __init__(self):
        self.contact = dict()
        
    def add_contact(self):
        self.name = input("Enter Name : ")
        self.phno = int(input("Enter Phone no : "))
        self.contact.update({self.name:self.phno})
        print("Contact added")
    
    def delete_contact(self):
        self.name = input("Enter Name : ")
        if self.name in self.contact.keys():
            self.contact.pop(self.name)
            print("Contact deleted")
        else:
            print("Contact not found")

    def view_contact(self):
        print("Name\tPhone No")
        for i in self.contact.keys():
            print(f"{i}\t{self.contact.get(i)}")

    def search_contact(self):
        self.name = input("Enter Name : ")
        if self.name in self.contact.keys():
            print(f"{self.name}\t{self.contact.get(self.name)}")
        else:
            print("Contact not found")
    
    def load_contact(self,filename):
        f = open(filename,"r")
        if f:
            for i in f:
                text = i.split("\t")
                self.contact.update({text[0]:int(text[1].strip())})
            print("Contacts loaded")
            self.view_contact()   
            
        else:
            print("file not found")
    
    def save_contact(self,filename):
        f = open(filename,"wt")
        if f:
            for i in self.contact.keys():
                f.write(f"{i}\t{self.contact.get(i)}\n")
            print("contact saved")
        else:
            print("Saving failed")
        
handler = ContactBook()
while(1):
    ch = int(input("1-Add Contact\n2-Delete Contact\n3-View Contact\n4-Search Contact\n5-Load Contact\n6-Save Contact\n7-Exit\n"))
    if ch == 1:
        handler.add_contact()
    elif ch == 2:
        handler.delete_contact()
    elif ch == 3:
        handler.view_contact()
    elif ch == 4:
        handler.search_contact()
    elif ch == 5:
        file = input("Enter file name : ")
        handler.load_contact(file)
    elif ch == 6:
        file = input("Save file as : ")
        handler.save_contact(file)
    elif ch == 7:
        break
    else:
        print("Invalid")