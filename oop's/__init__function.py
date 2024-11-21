class Student :
     #default constructors
     def __init__(self):
         pass
     #parameterized constructors
     
     def __init__(self,fullname,mark):
        self.name = fullname
        self.mark = mark
        print("adding new student in data base.......")
        
    
s1 = Student("pratik",37)
print(s1.name,s1.mark)


s2 = Student("shizuka",57)
print(s2.name,s2.mark)
