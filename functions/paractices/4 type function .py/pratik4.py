def factor(n):
    factorial=1 #2#6#24
    for i in range(1, n+1):  #1*2*3*4*5
        factorial=factorial*i  #1#2#6#24#120
    return factorial
print(factor(7))