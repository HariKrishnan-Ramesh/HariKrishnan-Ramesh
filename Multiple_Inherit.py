class Father:
    FatherName=""
    def father(self):
        print(self.FatherName)

class Mother:
    MotherName=""
    def mother(self):
        print(self.MotherName)

class Son(Father,Mother):
    def parents(self):
        print(f"Father name is {self.FatherName}")
        print(f"Mother name is {self.MotherName}")



s1=Son()
s1.FatherName = 'RAM'
s1.MotherName ='SITA'
s1.parents()