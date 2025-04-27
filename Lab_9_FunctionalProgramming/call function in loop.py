def fun():
    return print("func()")
def disp():
    return print("disp()")
def msg():
    return print( "msg()")
l=[fun,disp,msg]
for i in l:
    i()
