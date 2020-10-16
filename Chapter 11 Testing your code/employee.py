class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        self.name = f'{self.first_name.title()} {self.last_name.title()}'

    def give_raise(self, raise_amount = 5000):
        print(f'Employee name is {self.name}')
        self.annual_salary += raise_amount
        return self.annual_salary
