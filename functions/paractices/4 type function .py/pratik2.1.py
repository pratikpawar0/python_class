def absolute(n):
    s=str(n)
    if "-" in s[0]:
        print(int(s[1:]))
    else:
        print(n)