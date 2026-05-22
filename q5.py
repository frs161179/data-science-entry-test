def check_divisibility(num, divisor):
    if isinstance(num,(int,float)) and isinstance(divisor,(int,float)):
        #print(num%divisor)
        if num%divisor >0:
            print('number (num) is NOT divisible by another number (divisor)')
            return False
        else:
            print('number (num) is divisible by another number (divisor)')
            return True
    else:
        print('Number and divisor input should be integers or floats')
        return None

check_divisibility(10, 2)
check_divisibility(7, 3)



