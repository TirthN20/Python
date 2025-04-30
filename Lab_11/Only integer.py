n="h"
while type(n)!=int:
    try:
        n=int(input("Enter an integer : "))
        print(n)
    except ValueError :
        print("Enter only integer")
    
