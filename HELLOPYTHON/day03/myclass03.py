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
        
    def exercise(self, power):
        self.power_fly += power

        
class GaeSae(Dog, Bird):

    def __init__(self):
        Bird.__init__(self)
        Dog.__init__(self)
        

if __name__ == '__main__':
    gs = GaeSae()
    print(gs.power_bakr)
    print(gs.power_fly)
    gs.teachFromHuman()
    gs.exercise(5)
