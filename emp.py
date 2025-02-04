class EmployeeManagementSystem:
    def __init__(self):  # Corrected constructor name
        self.employees = []  # List to hold employee data

    def add_employee(self, employee_id, name, position, salary):
        """Adds a new employee."""
        employee = {
            'employee_id': employee_id,
            'name': name,
            'position': position,
            'salary': salary
        }
        self.employees.append(employee)
        print(f"Employee {name} added successfully.")

    def remove_employee(self, employee_id):
        """Removes an employee by employee_id."""
        for employee in self.employees:
            if employee['employee_id'] == employee_id:
                self.employees.remove(employee)
                print(f"Employee {employee_id} removed successfully.")
                return
        print(f"Employee with ID {employee_id} not found.")

    def update_employee(self, employee_id, name=None, position=None, salary=None):
        """Updates an existing employee's details."""
        for employee in self.employees:
            if employee['employee_id'] == employee_id:
                if name: employee['name'] = name
                if position: employee['position'] = position
                if salary: employee['salary'] = salary
                print(f"Employee {employee_id} updated successfully.")
                return
        print(f"Employee with ID {employee_id} not found.")

    def search_employee(self, employee_id):
        """Searches for an employee by employee_id."""
        for employee in self.employees:
            if employee['employee_id'] == employee_id:
                print(f"Employee Found: {employee}")
                return
        print(f"Employee with ID {employee_id} not found.")

    def list_all_employees(self):
        """Lists all employees."""
        if not self.employees:
            print("No employees found.")
            return
        print("Listing all employees:")
        for employee in self.employees:
            print(f"ID: {employee['employee_id']}, Name: {employee['name']}, Position: {employee['position']}, Salary: {employee['salary']}")

# Function to handle user interaction
def main():
    ems = EmployeeManagementSystem()
    
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Update Employee")
        print("4. Search Employee")
        print("5. List All Employees")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            employee_id = int(input("Enter Employee ID: "))
            name = input("Enter Employee Name: ")
            position = input("Enter Employee Position: ")
            salary = float(input("Enter Employee Salary: "))
            ems.add_employee(employee_id, name, position, salary)

        elif choice == '2':
            employee_id = int(input("Enter Employee ID to remove: "))
            ems.remove_employee(employee_id)

        elif choice == '3':
            employee_id = int(input("Enter Employee ID to update: "))
            name = input("Enter new Name (leave blank to keep current): ")
            position = input("Enter new Position (leave blank to keep current): ")
            salary_input = input("Enter new Salary (leave blank to keep current): ")
            salary = float(salary_input) if salary_input else None
            ems.update_employee(employee_id, name if name else None, position if position else None, salary)

        elif choice == '4':
            employee_id = int(input("Enter Employee ID to search: "))
            ems.search_employee(employee_id)

        elif choice == '5':
            ems.list_all_employees()

        elif choice == '6':
            print("Exiting the Employee Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
