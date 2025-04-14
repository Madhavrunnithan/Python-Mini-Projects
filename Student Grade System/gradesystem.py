class Student:
    subjects = ["Python","Compiler","Graphics","IEFT","AAD"]
    def __init__(self,name,roll):
        self.name = name
        self.rollno = roll
        self.marks = dict()
        self.average = 0
        self.grade = []

    def enter_marks(self):
        print("Enter marks :")
        for i in Student.subjects:
            mark = int(input(f"{i} : "))
            if mark > 90:
                grade = 'A'
            elif mark > 80:
                grade = 'B'
            elif mark > 70:
                grade = 'C'
            elif mark > 60:
                grade = 'D'
            else:
                grade = 'F'
            self.grade = [mark,grade]
            self.marks[i] = self.grade
        
    def calculate_avg(self):
        for i in self.marks.keys():
            self.average += int(self.marks[i][0])
        self.average = self.average/5
    
    def print_gradecard(self):
        if len(self.marks) == 0:
            print("No mark data\nEnter mark details to generate grade card")
        else:
            print(f"Student name : {self.name}\tRoll no : {self.rollno}")
            print(f"Subjects\tScore\tGrade")
            for subject in self.subjects:
                mark, grade = self.marks[subject]
                print(f"{subject:<15}{mark:<10}{grade}")
            self.calculate_avg()
            print("Average Score : ",self.average)
studentlist = dict()
while(1):
    ip = int(input("1-Open app\n2-Exit\n"))
    if ip == 1:
        roll = int(input("Enter roll No : "))
        if roll not in studentlist.keys():
            name = input("Enter name : ")
            stud = Student(name,roll)
            studentlist.update({roll : stud})
        stud = studentlist[roll]
        n = int(input("1-Enter mark details\n2-print gradesheet\n3-Exit\n"))
        if(n == 1):
            stud.enter_marks()
        elif n == 2:
            print("Gradecard :\n")
            stud.print_gradecard()
        else:
            print("Invalid")
    elif ip == 2:
        break
    else:
            print("Invalid")