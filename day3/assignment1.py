# 1. Using any of the conditional statement learnt to write a simple Python program that will 
# output the score and remark eg “Your score is 76 and this is Excellence” using the algorithm 
# below. Make sure that invalid score such value greater than 100 or less than 1 are detected 
# and reported 
#  0 – 34 = Fail 
#  35 – 44 = Pass 
#  45 – 49 = Fair 
#  50 – 59 = Good 
#  60 – 69 = Very Good 
#  70 – 100 = Excellence


score = 45
if score >=0 and score < 35:
    grade = 'f'
    print(f'your score is {score} and your grade is {grade}')
elif score >=35 and score < 45:
    grade = 'e'
    print(f'your score is {score} and your grade is {grade}')
elif score >=45 and score < 50:
    grade = 'd'
    print(f'your score is {score} and your grade is {grade}')
elif score >=50 and score < 60:
    grade = 'c'
    print(f'your score is {score} and your grade is {grade}')
elif score >=60 and score < 70:
    grade = 'b'
    print(f'your score is {score} and your grade is {grade}')
elif score >=70 and score <= 100:
    grade = 'a'
    print(f'your score is {score} and your grade is {grade}')
else:
    print(f'the score is invalid')

# 2. Write a program in python that will print the lowest number among three numbers supplied

num1 = 12
num2 = 13
num3 = 4
if num1 < num2 and num1 < num3:
    print(f'{num1} is less than {num2} and {num3}')
elif num2 < num1 and num2 < num3:
    print(f'{num2} is less than {num1} and {num3}')
elif num3 < num1 and num3 < num2:
    print(f'{num3} is less than {num1} and {num2}')
#asignment 2
#1. Create a multiplication table program using while loop, this will be done in such a way that when a

start = 1
number = 10
while start <= 12:
    result = number * start
    print(f'{number} x {start} = {result}')
    start += 1
#2. Write a program in python that tells if the name you supplied is in a list or the name is not in a lis
past_president = ['Buhari', 'Obasanjo', 'Jonathan', 'Abacha']
name = 'obasanjo'
convert_case = name.capitalize()
if convert_case in past_president:
    print(f'{convert_case} was once the president of nigeria')
else:
    print(f'{convert_case} has never been the president of nigria')
    for p in past_president:
        print(p)

#question 3
numbers = [10, 20, 30, 40, 70, 200, 300]
total = 0
for n in numbers:
    total += n
print(total)
print(total/len(numbers))
