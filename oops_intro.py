# class Instructor:
#     def __init__(self,instructor_name,subject,instagram_follower):
#         self.name = instructor_name
#         self.subject = subject
#         self.instagram_follower = instagram_follower
        

# Instructor1=Instructor('Akshay','Java',3000)
# print(Instructor1.name)
# print(Instructor1.subject)

class instructor:
    def __init__(self,name,adress):
        self.name=name
        self.adress=adress

    def display(self,name, subject):
        print('Hi')
        print(f"Hi My name is {name} and i teach {subject}")

instructor1 = instructor('Jenny','Gurgon')
print(instructor1.name)
instructor1.display('Hari','python')     
