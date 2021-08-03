from dask.array.random import power


class Dog:
    def __init__(self):
        self.power_bakr = 0
        
    def teachFromHuman(self):
        self.power_bakr += 1
       
class Bird(Dog):
    def __init__(self):
#         dog.__init__(self)
#        이렇게 해도 위에 것과 같다

        super().__init__()
        self.power_fly = 0
        
    def exercise(self,power):
        self.power_fly += power
   

if __name__ == '__main__':
    bird = Bird()
    print(bird.power_bakr)
    bird.teachFromHuman()
    print(bird.power_bakr)
    
    print()
    
    print(bird.power_fly)
    bird.exercise(5)
    print(bird.power_fly)
    
    print()
    
    dog = Dog()
    print(dog.power_bakr)
    dog.teachFromHuman()
    print(dog.power_bakr)
    
    
    
    
