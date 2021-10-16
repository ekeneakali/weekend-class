class Employee():
    pay_rise = 0.05

#constructor method in class
    def __init__(self):
        print('this is a constructor')

#method in class
    def details(self):
        return 'here is the product details'

e1 = Employee()
print(e1.pay_rise)
print(e1.details())
