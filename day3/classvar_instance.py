class Employee():
    pay_rise = 0.05

#constructor method in class
    def __init__(self, firstname, lastname, pay):
        self.f = firstname
        self.l = lastname
        self.p = pay
        #a class variable which object changes
        print('this is a constructor')

#method in class
    def details(self):
        return 'here is the product details'

e1 = Employee('benedict', 'uwazie', 1500)
print(e1.pay_rise)
print(e1.f)
print(e1.l)
e2 = Employee('alabi', 'adebayor', 2500)
print(e2.pay_rise)
print(e1.f)
print(e1.l)

