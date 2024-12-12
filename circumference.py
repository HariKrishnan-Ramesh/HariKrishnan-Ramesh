class circumference:
    def __init__(self,radius):
        self.radius=radius
        circumference=3.14*radius*radius
        print(f"circumeference if a circle is {circumference}")

rads=int(input("Enter the radius: "))
answer=circumference(rads)
        