def update_dictionary(dct, key, value):
    if isinstance(dct, dict):
        #print(len(dct))
        if len(dct) <= 0:
            dct.update({key: value})
        else:
            for x, y in dct.items():
                if x == key:
                    print('Original value: '+x,y)
                    dct.update({key:value})
        print(dct)
    else:
        print('Not a dictionary')

update_dictionary({}, "name", "Alice")
update_dictionary({"age": 25}, "age", 26)






