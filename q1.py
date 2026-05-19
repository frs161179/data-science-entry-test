def swap(x, y):
    if isinstance(x,str):
        return -1
    elif isinstance(y,str):
        return -1
    elif isinstance(x,(int,float)) and isinstance(y,(int,float)):
        temp=x
        x = y
        y=temp
        print('value x: '+str(x))
        print('value y: '+str(y))
        return 0
    else:
        return -1

swap("Apple",10)
swap(9,17)











