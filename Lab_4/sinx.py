def fact(n):
    q=1
    for i in range(1,n+1) :
        q=q*i
    return q



x=float(input("Enter degrees : "))
rad=((3.14159)/180)*x
a=rad - (rad**3)/fact(3) + (rad**5)/fact(5) - (rad**7)/fact(7)
print("sinx : ",a)
