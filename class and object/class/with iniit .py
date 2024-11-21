#with __init__
class Animal:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def show_info(self):
        print(f"The animal name is:{self.name} and color is {self.color}")
object=Animal("tiger","yellow")

object.show_info()   