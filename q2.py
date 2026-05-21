def find_and_replace(lst, find_val, replace_val):

    if not isinstance(lst,list):
        return 'Input is not List !!'
    else :

            i = 0
            while i < len(lst):
                if (lst[i]) == find_val:
                    lst[i]=replace_val
                i += 1
            return lst

print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))













