class Bird:
    def sound(self):
        return "Some gereric bird sound"
    
class Sparrow(Bird):
    def sound(self):
        return "Chirp Chirp"
    
class Crow(Bird):
    def sound(self):
        return "Caw Caw"
    
for bird in[Sparrow(), Crow(), Bird()]:
    print(bird.sound())