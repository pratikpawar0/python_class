count=0  #2
s=str(input("enter your string:"))  #python
target=str(input("enter the target char:"))#n
for i in s:
    if target==i:
        count=count+1
print(count)