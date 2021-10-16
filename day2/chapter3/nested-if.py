a = '15'
b = '15'

if a == b:
    if a.isnumeric() and b.isnumeric():
        result = int(a) * int(b)
        print(result)
        #if inside another if