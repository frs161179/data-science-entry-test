def find_first_negative(lst):
    if not isinstance(lst,list):
        return 'Input is not List !!'
    else :
        i = 0
        while i < len(lst):
            if (lst[i]) < 0 :
                #Return the first negative number if found
                return 'first negative number if found : ' + str(lst[i])
            i += 1
        #otherwise return "No negatives"
        return 'No negatives'


print(find_first_negative([3, 5, -1, 7, -2, 8]))
print(find_first_negative([2, 10, 7, 0]))




