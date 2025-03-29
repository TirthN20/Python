def create_array(l1,b1,h1,n):
    
    height=[n]*h1
    breadth=[height]*b1
    length=[[breadth]*l1]
    print(length)
            

l1=int(input("Enter length : "))
b1=int(input("Enter breadth : "))
h1=int(input("Enter height : "))
n=int(input("Enter element : "))

create_array(l1,b1,h1,n)
