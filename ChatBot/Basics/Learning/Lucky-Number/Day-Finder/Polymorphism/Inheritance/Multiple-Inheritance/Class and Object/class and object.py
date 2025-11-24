class Student:
    def __int__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Dhruva", 95)
s1.display()

