def count_alpha_digits(a):
    alp=0
    dig=0
    for i in a :
        if i.isalpha() :
            alp+=1
        elif i.isdigit() :
            dig+=1
    dict={'alphabets ':alp,'numbers':dig}
    print(dict)





a=input("Enter a string : ")
count_alpha_digits(a)
