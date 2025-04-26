def ab(a,b):
    if b==0:
        return 1
    else :
        return a*ab(a,b-1)


a=int(input("Enter base :"))
b=int(input("Enter power :"))
print(ab(a,b))
