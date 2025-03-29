def create_list(l1,l2):
    l3=[]
    for i in l1 :
        if i in l2 :
            l3.append(i)
    print(list(set(l3)))
        




l1=[]
l2=[]
for i in range(0,5):
    l1.append(int(input("Enter element of l1 : "))) 
    l2.append(int(input("Enter element of l2 : ")))
print(l1)
print(l2)    
create_list(l1,l2)   
