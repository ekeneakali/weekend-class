firstname = 'ekene'
lastname = 'akali'
with open('data.txt', 'a') as f:
    f.write('\n' + firstname + ' '+lastname)
#this to write file to another file