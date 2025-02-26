a=input("Enter a string : ")
b=""
for i in a :
    if (65<=ord(i)<=90) :
        b=b+chr(ord(i)+32)
    elif (97<=ord(i)<=122) :
        b=b+chr(ord(i)-32)
print(b)
        
