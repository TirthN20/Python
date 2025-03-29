def ispalindrome(a):
    check=''.join(a.lower().split())
    
    s=''
    print(check)
    for i in range(len(a)-1,-1,-1):
        s=s+a[i]
    b=''.join(s.lower().split())
    if b==check :
        print("PALINDROME")
    else :
        print("NOT PALINDROME")
        





a=input("Enter a string : ")
ispalindrome(a)
