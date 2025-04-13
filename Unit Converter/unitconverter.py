class units:
    def metertofeet(self,l):
        self.result = l*3.28084
        return f"{self.result} ft"

    def kgtopound(self,kg):
        self.result = kg*2.205
        return f"{self.result} Ibs"
    
    def degctodegf(self,c):
        self.result = (c*(9/5)) + 32
        return f"{self.result} °F"
    
    def litrestogallons(self,li):
        self.result = 0.264172 * li
        return f"{self.result} gal"
    
    def mintohours(self,min):
        self.result = min/60
        return f"{self.result} hrs"
    
    def readunit(self,choices,ch):
        ip = float(input(f"Enter {choices.get(ch)} : "))
        if ch == 1:
            self.res = self.metertofeet(ip)
            print(self.res)
        elif ch == 2:
            self.res = self.kgtopound(ip)
            print(self.res)
        elif ch == 3:
            self.res = self.degctodegf(ip)
            print(self.res)
        elif ch == 4:
            self.res = self.litrestogallons(ip)
            print(self.res)
        elif ch == 5:
            self.res = self.mintohours(ip)
            print(self.res)

converter = units()
choices = {1:"Meter",2:"kg",3:"°C",4:"Litres",5:"minutes"}
while(1):
    ch = int(input("1-meters to feet\n2-kg to Ibs\n3-°C to °F\n4-Liters to Gallons\n5-minutes to hour\n6-Exit\n\nEnter choice : "))
    if ch not in [1,2,3,4,5,6]:
        print("Invalid")
    elif ch == 6:
        break
    else:
        converter.readunit(choices,ch)
        print("\n\n")