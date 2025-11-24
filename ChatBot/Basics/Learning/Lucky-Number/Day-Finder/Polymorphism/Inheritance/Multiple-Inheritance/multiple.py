class Father:
    def skills(self):
        print("father: Gardening and Painting")

class Mother:
    def skills(self):
        print("Mother: Cooking and Dancing")

class Child(Father,Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Child: Singing and Coding")

c = Child()
c.skills()