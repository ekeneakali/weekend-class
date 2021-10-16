# # 
# var1 = 2
# var2 = 0
# print(var1/var2)

#the second one is more preferable
import datetime


try:
    var1 = 2
    var2 = 0
    print(var1/var2)
except ZeroDivisionError as e:
    print(f'this is a {e} error')
#to put error message in a file

    with open('error.txt', 'a') as f:
        date = datetime.datetime.now()
        error = f'{date} this is a {e} error'
        f.write('\n'+error)