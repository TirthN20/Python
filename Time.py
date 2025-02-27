for i in range(0,25) :
    if i==0 :
        print("Midnight")
    elif 0<i<12 :
        print(i,"AM")
    elif i==12 :
        print("Noon")
    elif 12<i<24 :
        print(i-12,"PM")
