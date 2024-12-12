class circumference():
    def __init__(self,radius):
        self.radius=radius

    def circle(self):
        circumference=2 * 3.14 * self.radius
        print(f"circumeference if a circle is {circumference}")

rads=int(input("Enter the radius: "))
answer=circumference(rads)
answer.circle()
        