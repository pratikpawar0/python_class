#round up 
def round_up(a):
    decimal_part=a-int(a)
    if decimal_part>=0.5:
        print(int(a)+1)
    else:
        print(int(a))
        