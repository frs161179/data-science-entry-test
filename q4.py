def string_reverse(s):
    if isinstance(s, str): #s must be a string
        #print(len(s))
        i = 0
        s_rev = ''
        length = len(s)
        while i < length:
            s_rev = s_rev + s[length - i - 1] #reverses a given string
            i+=1
        #Return the reversed string.
        return 'Original string: '+s+ '\nString reverse : '+s_rev
    else:
        return 'Input must be string'

print(string_reverse("Hello World"))
print(string_reverse("Python"))



