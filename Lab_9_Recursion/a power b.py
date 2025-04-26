def power(a,b):
    if b==0 :
        return 1
    while b!=0:
        return a*power(a,b-1)




a=int(input("enter base : "))
b=int(input("enter power : "))
print(power(a,b))
