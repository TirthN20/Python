def sum_avg(a1,a2,a3,a4,a5):
    sum=(a1+a2+a3+a4+a5)
    avg=sum/5
    return sum,avg
    



a1=int(input("Enter marks of subject 1 : "))
a2=int(input("Enter marks of subject 2 : "))
a3=int(input("Enter marks of subject 3 : "))
a4=int(input("Enter marks of subject 4 : "))
a5=int(input("Enter marks of subject 5 : "))
print(sum_avg(a1,a2,a3,a4,a5))
