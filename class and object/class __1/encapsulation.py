#public member i
class bike:
    name="tvs"
    def ride(self):
        print("gift for youhh")
object=bike()
object.ride
object.name

#protected member 
class base :
    def __init__(self):
        self._a =2 
class derived(base):
    def protected(self):
        print("calling protected member of base class " ,self._a)
object = derived()
object.protected()
object._a        
        