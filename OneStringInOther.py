def check():
    a=input("Enter first string : ")
    b=input("Enter second string : ")
    if (a in b) :
        print("First string is present in second string ")
    elif (b in a) :
        print("Second string is present in first string ")
    else :
        print("No common strings present ")
check()
check()
