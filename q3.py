def update_dictionary(dct, key, value):
    if isinstance(dct, dict): #input must be dictionary
        #print(len(dct))
        if len(dct) <= 0: #if empty dictionary, add value
            dct.update({key: value})
        else:
            for x, y in dct.items():
                if x == key: #If the key already exists in dct, print the original value, then update its value.
                    print('Original value: '+x,y)
                    dct.update({key:value})
        return dct #Return the updated dictionary.
    else:
        print('Not a dictionary')
        return None

print(update_dictionary({}, "name", "Alice"))
print(update_dictionary({"age": 25}, "age", 26))








