#Write a program that reads a string from the keyboard and creates dictionary containing frequency
#of each character occurring in the string.

a=input("Enter a string : ")
b={}
for i in a :
    x=a.count(i)
    b.update({i:x})
print(b)
