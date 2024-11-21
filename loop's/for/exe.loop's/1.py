 #suum of number 


total = 0
for i in range (1,100):
    total=total+i
print(total)



#2nd  method

n = int(input("enter the range"))
total = 0
for i in range(1,n+1):
    total+=i
    print(total)


n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(i)           
    
    
l=[]
n = int(input("Enter a number: "))
for i in range(1, n+1):
    l.append(i*i)
print(l)                    


l=[]
n = int(input("Enter a number: "))
for i in range(1, n+1):
    l.append(i)
print(l)



l=[]
n = int(input("Enter a number: "))
for i in range(1, n+1):
    x=i*i
    l.append(x)
print(l)







sqaures=[]
for i in range(1,11):
    sqr=i**2
    sqaures.append(sqr)
print(sqaures)