grades = eval(input("Enter the marks:"))
total = 0  #initialize
for marks in grades:
    total += marks  #total=total+marks
average = total / len(grades)
print("total:",total,"Average Grade:", average)
print(f"total:{total} Average Grade: {average}")
