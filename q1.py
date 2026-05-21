def swap(x, y):
    if isinstance(x,str):
        print('-1')
    elif isinstance(y,str):
        print('-1')
    elif isinstance(x,(int,float)) and isinstance(y,(int,float)):
        temp=x
        x = y
        y=temp
        print('value x: '+str(x))
        print('value y: '+str(y))
    else:
        print('-1')

swap("Apple",10)
swap(9,17)













