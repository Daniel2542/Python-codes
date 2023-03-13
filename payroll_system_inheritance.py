#creating a payroll system using inheritance

class Payroll_System:
    def calculate_payroll(self, employees):
        print('Payroll Calculator'"\n")
        for employee in employees:
            print(f'Payroll for: {employee.id}){employee.name}')
            print(f' Amount: {employee.calculate_payroll()}')
            print('')
class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name
class Salaried_Employee(Employee):
    def __init__(self,id,name,monthly_salary):
        super().__init__(id, name)
        self.monthly_salary = monthly_salary
    def calculate_payroll(self):
        return self.monthly_salary
    
class Hourly_Employee(Employee):
    def __init__(self,id,name,hours_worked,hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate
    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate
    
class Commission_Employee(Salaried_Employee):
    def __init__(self,id,name,monthly_salary,commission):
        super().__init__(id, name,monthly_salary)
        self.commission=commission
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission
    