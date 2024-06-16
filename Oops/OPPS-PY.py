class Employee:
    def __init__(self, emp_name, emp_salary, dept, domain, month):
        self.name = emp_name
        self.__salary = emp_salary  # private variable
        self.dept = dept
        self.domain = domain
        self.__month = month  # private variable

    def __information(self):  # private method
        print('\t-:-- JAMES-STREET --:-')
        print(f'Name of Employee: {self.name}')
        print(f'Name of Department: {self.dept}')
        print(f'Employment: {self.domain}')

    def calculate(self):
        self.__information()
        
        def amount(months, salary): 
            return months * salary

        print(f'Salary Is: Rs {amount(self.__month, self.__salary)}')


if __name__ == '__main__':
    name = input('Enter your Name: ')
    salary = int(input('Enter Your Salary: '))
    employment, domain = input('Enter your Domain & Employment: ').split()
    months = int(input('Enter Your Month: '))

    miraj = Employee(name, salary, domain, employment, months)
    miraj.calculate()
