class Employee():
    pay_rise = 0.05


    def __init__(self, firstname, lastname, pay):
        self.f = firstname
        self.l = lastname
        self.p = pay
        
        print('this is a constructor')

    def salary(self):
        increase = self.p * self.pay_rise
        salary = increase + self.p
        return salary


    def details(self):
        return 'here is the product details'

e1 = Employee('benedict', 'uwazie', 2000)
print(e1.salary())

class Developer(Employee):
    #pass
    def my_details(self):
        return f'my firstname is {self.f} and lastname {self.l}'
d1 = Developer('alabi', 'adebayor', 4000)
print(d1.my_details())
print(d1.salary())

    

