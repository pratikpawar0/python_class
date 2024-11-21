#without init/.........
class myself :
    def my_intro(self,name,sex,live):
        self.name =name
        self.sex = sex
        self.live =live
    def my_name(self):
        return f"and my name is {self.my_name}"
    def my_sex(self):
        return f"& i am {self.sex} "
   
    def my_live(self):
        return f" form a {self.live}"
    
object = myself()    
object.my_intro("pratik","boy","betul")
print(object.my_name())
print(object.my_sex())
print(object.my_live())
    
