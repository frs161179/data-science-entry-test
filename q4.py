def string_reverse(s):
    if isinstance(s, str):
        #print(len(s))
        i = 0
        s_rev = ''
        length = len(s)
        while i < length:
            s_rev = s_rev + s[length - i - 1]
            i+=1
        print('Original string: '+s)
        print('String reverse : '+s_rev)
    else:
        print('Input must be string')

string_reverse("Hello World")
string_reverse("Python")

