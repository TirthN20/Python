def num():
    a=input("Enter a string : ")
    cha=0
    dig=0
    for i in range(0,len(a)) :
        if a[i].isalpha()==True :
            cha=cha+1
        elif a[i].isdigit()==True :
            dig=dig+1
    print("The number of alphabets are : ",cha)
    print("The number of digits are : ",dig)
num()
