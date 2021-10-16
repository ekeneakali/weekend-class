def say_hello():
    print('hello world')

say_hello()

def greetings(name):
    print(f'hello {name}')

greetings('alabi')
greetings('benedict')

def full_name(firstname, lastname):
    print(f'my full name is {firstname} {lastname}')

full_name('ekene', 'akali')

def history(firstname, gender, age):
    print(f'my name is {firstname} i am {gender} by gender am {age} years old')

history('benedict', 'male', 45)
history('ekene', 'male', 25)

def add_numbers(num1, num2):
    add = num1 + num2
    print(add)
add_numbers(10, 15)

# area = 1/2 * base * height
def area_triangle(base, height):
    area = 0.5 * base * height
    print(area)
area_triangle(100, 50)
area_triangle(200, 100)

def perimeter(width, breath):
    peri = 2 + width + breath
    print(peri)
perimeter(300, 50)
# function that take a default value
def office(name, color='yellow'):
    print(f'the color of {name} is {color}')

office('mtn')
office('alabian', 'sky blue')

def print_even(stop, start=1):
    for n in range(start, stop+1):
        if n % 2 == 0:
            print(n)
print_even(10)
print('BREAK')
print_even(15, 3)