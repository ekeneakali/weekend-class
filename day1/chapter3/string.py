string1 = 'get rich or die trying by "50 cent" '
print(string1)
string2 = "get rich or die trying by '50 cent' "
print(string2)
string3 = "get rich or die trying by \"50 cent\" "
print(string3)
firstname = 'ekene '
lastname = 'akali'
fullname = firstname + lastname
#another to concatenate in python
#fullname = firstname'  '+lastname
print(fullname)
name = 'ekene'
age = 25
color = 'fair'
sentence1 = 'my name is '+name+', i am '+str(age)+'years old and '+color+' in complexion'
print(sentence1)
sentence2 = 'my name is {}, i am {}years old and {} in complexion'.format(name, age, color)
print(sentence2)
sentence3 = f'my name is {name}, i am {age}years old and {color} in complexion'
#INDEXING AND SLICING IN PYTHON
print(sentence3)
print('INDEXING')
name = 'benedict'
print(name[0])
print('SLICING')
print(name[:3])
print(name[3:])
print(name[2:5])
