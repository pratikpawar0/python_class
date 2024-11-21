class overloadingExample :
    def add (self,a,b):
         print(a+b)
    def add (self,a,b,c=4):
        print(a+b+c)
a=overloadingExample()
a.add(5,10)
a.add(5,10,30)    

#class overloadingExample :
   # def add (self,a,b):
    #     print(a+b)
    #def add (self,a,b,c):
     #   print(a+b+c)
#a=overloadingExample()
#a.add(5,10)
#a.add(5,10,30)            


# method overloding parent class behaves differnrtly in 

        