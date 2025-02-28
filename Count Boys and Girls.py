lst=[('Tirth','Prince'),'Heer','Krissa']
cB=0
cG=0
for i in lst :
    if isinstance(i,tuple) :
        for j in i :
            cB+=1
    else :
        cG+=1
print("The number of boys are : ",cB)
print("The number of girls are : ",cG)
                    
        
