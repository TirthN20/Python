def count_lower_upper(a):
    countL=0
    countU=0
    for i in a:
        if i.isupper():
            countU+=1
        elif i.islower():
            countL+=1
    d={'Lower':countL,'Upper':countU}
    print(d)
            
        





s=input("Enter a string : ")
count_lower_upper(s)
