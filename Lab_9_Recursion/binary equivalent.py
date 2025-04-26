def binary(n):
    if n==1:
        return "1"
    else :
        return binary(n//2)+str(n%2)

n=int(input("Enter a number : "))
print(binary(n))
