def pangram(s):
    s1={chr(i) for i in range(65,91)}
    print(s1)
    s2=set(s.upper())
    print(s2)
    if s1.issubset(s2):
        print("PANGRAM")
    else :
        print("NOT PANGRAM")
s=input("Enter a string : ")
pangram(s)
