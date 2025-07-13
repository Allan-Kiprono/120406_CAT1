class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, ID: {self.employee_id}, Salary: KES{self.salary:.2f}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Updated salary for {self.name} to KES{self.salary:.2f}")


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []  # list of Employee objects

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added employee {employee.name} to department {self.department_name}.")

    def total_salary_expenditure(self):
        total = sum(emp.salary for emp in self.employees)
        print(f"Total salary expenditure for {self.department_name}: KES{total:.2f}")
        return total

    def display_all_employees(self):
        if not self.employees:
            print("No employees in this department.")
            return
        print(f"\nEmployees in {self.department_name}:")
        for emp in self.employees:
            emp.display_details()


# Interactive system
def run_department_interface():
    dept_name = input("Enter department name: ")
    department = Department(dept_name)

    while True:
        print("\n--- Department Menu ---")
        print("1. Add Employee")
        print("2. Update Employee Salary")
        print("3. Display All Employees")
        print("4. Show Total Salary Expenditure")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter employee name: ")
            emp_id = input("Enter employee ID: ")
            try:
                salary = float(input("Enter salary: "))
                employee = Employee(name, emp_id, salary)
                department.add_employee(employee)
            except ValueError:
                print("Invalid salary input. Please enter a number.")

        elif choice == "2":
            emp_id = input("Enter employee ID to update salary: ")
            employee = next((e for e in department.employees if e.employee_id == emp_id), None)
            if employee:
                try:
                    new_salary = float(input("Enter new salary: "))
                    employee.update_salary(new_salary)
                except ValueError:
                    print("Invalid salary input.")
            else:
                print("Employee not found.")

        elif choice == "3":
            department.display_all_employees()

        elif choice == "4":
            department.total_salary_expenditure()

        elif choice == "5":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


# Run the program
run_department_interface()
