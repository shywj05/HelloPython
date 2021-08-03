class Animal:
    def __init__(self): 
        self.age = 1
    def getOld(self):
        self.age+=1
        
class Human(Animal):
    def __init__(self):
        super().__init__()
        self.power_lang = 1
    
    def learn_lang(self):
        self.power_lang += 1
        
    def pt(self,power):
        self.power_lang += power
        
        

if __name__ == '__main__':
    ani = Animal()
    print(ani.age)
    ani.getOld()
    print(ani.age)
    
    hum = Human()
    print(hum.age)
    hum.getOld()
    print(hum.age)
    hum.learn_lang()
    print(hum.power_lang)
    hum.pt(5)
    print(hum.power_lang)
    