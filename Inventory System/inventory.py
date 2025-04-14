class Inventory:
    def __init__(self):
        self.stack = dict()
        self.itemdetails = []
        
    
    def add_item(self,item,quantity,price):
        self.itemdetails = [quantity,price]
        self.stack[item] = self.itemdetails
        print("Item added")

    def delete_item(self,item):
        if item in self.stack.keys():
            self.stack.pop(item)
            print("Item Removed")
        else:
            print("Item not found")
    
    def search_item(self,item):
        if item in self.stack.keys():
            print("Item found")
            print(f"{item} Quantity({self.stack[item][0]} Price({self.stack[item][1]}))")
        else:
            print("item not found")
        
    def update_item(self,item):
        if item in self.stack.keys():
            q = int(input("Quantity : "))
            p = int(input("Price : "))
            self.stack[item] = [q,p]
            print("Item Updated")
        else:
            print("Item not found")

    def show_item(self):
        print(f"Item\t   Quantity\tPrice/kg:")
        for item in self.stack.keys():
            q, p = self.stack[item]
            print(f"{item:<15}{q:<15}{p}/kg")

inv = Inventory()
while(1):
    n = int(input("1-Add item\n2-Delete items\n3-Search item\n4-Update item\n5-Show items\n6-exit\n"))
    if n == 1:
        item = input("Item name : ")
        quantity = int(input("Quantity : "))
        price = int(input("Price : "))
        inv.add_item(item,quantity,price)
    elif n == 2:
        item = input("Item name : ")
        inv.delete_item(item)
    elif n == 3:
        item = input("Item name : ")
        inv.search_item(item)
    elif n == 4:
        item = input("Item name : ")
        inv.update_item(item)
    elif n == 5:
        inv.show_item()
    elif n == 6:
        break
    else:
        print("invalid")
        