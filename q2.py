def find_and_replace(lst, find_val, replace_val):

    if not isinstance(lst,list): #lst must be a list
        return 'Input is not List !!'
    else :
        #lst is a list
            i = 0
            while i < len(lst):
                if (lst[i]) == find_val: #searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val) once found
                    lst[i]=replace_val #replaces them with another value (replace_val) when condition is met
                i += 1
            return lst

print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))













