class Animal :
    def info(self,name,color):
        self.name=name
        self.color=color
    def show_info(self):
        print(f"The animal name is:{self.name} and color is {self.color}")
object =Animal()  #object created
object.info("tiger","yellow")
object.show_info()        
        
n=Animal()
n.info("loin","yellow")
n.show_info()        
        

