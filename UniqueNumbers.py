def prime(n):
    t=1
    for i in range(2,n):
        if n%i==0 :
            t=1
        
    if t==0 :
        print("Prime Number")
        
def perfect(n):
    t=0
    z=n//2
    sum=0
    for i in range(1,z+1):
        if n%i==0 :
            sum=sum+i
    if sum==n :
        print("Perfect Number")

def armstrong(n):
    summ=0
    rem=0
    check=n
    while n>0 :
        
        rem=n%10
        summ=rem*rem*rem+summ
        n=n//10
        
      
    if summ==check :
        print("Armstrong Number")
    
                
a=int(input("Enter a number : ")) 
prime(a)
perfect(a)
armstrong(a)
  
       
    
