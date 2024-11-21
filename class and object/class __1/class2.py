#with in init 
class car :
    def __init__(self ,name ,speed ,color ):
        self.name = name 
        self.speed = speed
        self.color = color
    def  spacification(self):
        print("the car name is ", self.name ," & color is ",self.color)
    def speed1(self):
            print ("and speed is ",self.speed)
object1 = car("bmw","black","250km")
object1.spacification()
object1.speed1()





