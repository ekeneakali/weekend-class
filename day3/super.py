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
    def __init__(self, firstname, lastname, pay, prog_lang):
        super().__init__(firstname, lastname, pay)
        self.pro = prog_lang
    def my_details(self):
        return f'my firstname is {self.f} and lastname {self.l}'
d1 = Developer('alabi', 'adebayor', 4000, 'php')
print(d1.my_details())
print(d1.salary())
print(d1.pro)

    

