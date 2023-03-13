import payroll_system_inheritance

salary_employee = payroll_system_inheritance.Salaried_Employee(1, 'Daniel Wainaina', 20000)
hourly_employee = payroll_system_inheritance.Hourly_Employee(2, 'Martin Njue', 1000, 15)
commission_employee = payroll_system_inheritance.Commission_Employee(3, 'Danny', 10000, 250)
payroll_system = payroll_system_inheritance.Payroll_System()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee
])    