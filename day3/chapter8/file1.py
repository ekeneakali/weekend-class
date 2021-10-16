# f = open('demo.txt', 'r')
# for p in f:
#     print(p, end='')
# f.close()

with open('demo.txt', 'r')as f:
    for p in f:
        print(p, end='')
        

#this is use to read file in another file