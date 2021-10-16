
import my_module


class Developer(my_module.Employee):
    #pass
    def my_details(self):
        return f'my firstname is {self.f} and lastname {self.l}'



d1 = Developer('alabi', 'adebayor', 4000)
print(d1.my_details())
print(d1.salary())

my_module.print_even(12, 5)
