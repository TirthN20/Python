def compute(n):
    sum=n
    check=n
    for i in range(1,n):
        check=check*10+n
        sum=check+sum
    print(sum)

n=int(input("Enter a number : "))
compute(n)
