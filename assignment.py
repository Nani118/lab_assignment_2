class Employee:
    def _init_(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def _str_(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"


def sort_employee_data(employees, sort_param):
    if sort_param == 1:
        return sorted(employees, key=lambda emp: emp.age)
    elif sort_param == 2:
        return sorted(employees, key=lambda emp: emp.name)
    elif sort_param == 3:
        return sorted(employees, key=lambda emp: emp.salary)
    else:
        print("Invalid sorting parameter")
        return employees


if __name__ == "_main_":
    employee_data = [
        Employee("161E90", "Ramu", 35, 59000),
        Employee("171E22", "Tejas", 30, 82100),
        Employee("171G55", "Abhi", 25, 100000),
        Employee("152K46", "Jaya", 32, 85000),
    ]

    print("Employee Data:")
    for employee in employee_data:
        print(employee)

    try:
        sorting_parameter = int(input("\nEnter sorting parameter (1. Age, 2. Name, 3. Salary): "))
        sorted_employees = sort_employee_data(employee_data, sorting_parameter)

        print("\nSorted Employee Data:")
        for employee in sorted_employees:
            print(employee)
    except ValueError:
        print("Invalid input. Please enter a number.")