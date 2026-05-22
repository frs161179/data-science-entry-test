def check_divisibility(num, divisor):
    if isinstance(num,(int,float)) and isinstance(divisor,(int,float)): #Both num and divisor must be numeric.
        #print(num%divisor)
        if num%divisor >0: #Return False if num is NOT divisible by divisor
            return False
        else: #Return True if num is divisible by divisor
            return True
    else:
        print('Number and divisor input should be integers or floats')
        return None

print(check_divisibility(10, 2))
print(check_divisibility(7, 3))






