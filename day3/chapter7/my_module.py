
class Employee():
    pay_rise = 0.1

#constructor method in class
    def __init__(self, firstname, lastname, pay):
        self.f = firstname
        self.l = lastname
        self.p = pay
        print('this is a constructor')

#method in class
    def salary(self):
        increase = self.p * self.pay_rise
        salary = increase + self.p
        return salary
    def details(self):
        return 'here is the product details'

def print_even(stop, start=1):
    for n in range(start, stop+1):
        if n % 2 == 0:
            print(n)