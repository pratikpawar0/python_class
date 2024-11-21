#if and else statement 

a=int(input("enter a 1 st num .:"))
b=int(input("enter a 2 nd num.:"))   
if a==b:
    print ("a equa to b ") 
else:
    print("a cant equal to b") 
    
# odd and even num 
num = int(input("enter a number "))
if num % 2 == 0:
    print(num ," is an even num .")
else:
    print (num,"is an odd num")


# check age for voting 
a=int(input("Enter age: "))
if a>=18:
    print("you can vote")
else:
    print("You are not eligible")
    
#larger two num 


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print("The larger number is:", num1)
else :
    print("The larger number is:", num2)


#smaller two num

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 < num2:
    print("The smaller number is:", num1)
else :
    print("The smaller number is:", num2)
    



#find a maximum of three num
n1=150
n2=9
n3=120
if n1>n2 and n1>n3:
    print("greater is :",n1)
elif n2>n3 and n2>n1 :
    print("greater is :",n2)
else: 
    print("greater is :",n3)

n1=62
n2=9
n3=0
if n1<n2 and n1<n3:
    print("smaller is :",n1)
elif n2<n3 and n2<n1 :
    print("smaller is :",n2)
else: 
    print("smaller is :",n3)






