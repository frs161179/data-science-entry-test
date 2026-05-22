def swap(x, y):

    if isinstance(x,(int,float)) and isinstance(y,(int,float)): #x and y must be numeric
        temp=x #store x variable value to temporary variable for swap preparation
        x = y # x value is swapped to y
        y=temp # y value is swapped to x (thanks to temporary variable)
        return 'value x: '+str(x) + ' and value y: '+str(y)
    else:
        return '-1'

print(swap("Apple",10))
print(swap(9,17))

'''
Francis notes:
* q1 question requirement are following:
- x AND y must be numeric
- print the swapped values if both x AND y are numeric

therefore I'm assuming following requirement is human typo:
- Return -1 if x and y is not numeric, and
* should be return -1 if EITHER x OR y is not numeric --> since the requirement is "x AND y must be numeric"
'''

















