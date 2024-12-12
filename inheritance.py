class Human:
    def __init__(self,name,):
        self.name=name
        
    def eat(self):
        print("I can Eat")
    
    def work(self):
        print("I can Work")

class Male(Human):
    def flirt(self):
        print("I can Flirt")
    
    def work(self):
        super().work()
        print("I can Code")
    
male1=Male()
male1.eat()
male1.work()