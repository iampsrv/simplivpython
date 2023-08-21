employees = []

def add_employee():
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    position = input("Enter employee position: ")

    employee = {
        'name': name,
        'age': age,
        'position': position
    }

    employees.append(employee)
    print("Employee added successfully.")

def search_employee():
    name = input("Enter employee name to search: ")

    for employee in employees:
        if employee['name'] == name:
            print_employee_details(employee)
            return

    print("Employee not found.")

def print_employee_details(employee):
    print("Employee Details:")
    print("Name:", employee['name'])
    print("Age:", employee['age'])
    print("Position:", employee['position'])
    print()

def update_employee():
    name = input("Enter employee name to update: ")

    for employee in employees:
        if employee['name'] == name:
            print_employee_details(employee)
            new_name = input("Enter new name (leave blank to keep current): ")
            new_age = input("Enter new age (leave blank to keep current): ")
            new_position = input("Enter new position (leave blank to keep current): ")

            if new_name:
                employee['name'] = new_name
            if new_age:
                employee['age'] = int(new_age)
            if new_position:
                employee['position'] = new_position

            print("Employee details updated successfully.")
            print_employee_details(employee)
            return

    print("Employee not found.")

def delete_employee():
    name = input("Enter employee name to delete: ")

    for employee in employees:
        if employee['name'] == name:
            print_employee_details(employee)
            confirm = input("Are you sure you want to delete this employee? (y/n): ")

            if confirm.lower() == 'y':
                employees.remove(employee)
                print("Employee deleted successfully.")
            else:
                print("Deletion canceled.")
            return

    print("Employee not found.")

def display_employees():
    if not employees:
        print("No employees found.")
    else:
        print("Employee List:")
        for employee in employees:
            print_employee_details(employee)

def main_menu():
    while True:
        print("Employee Management System")
        print("1. Add Employee")
        print("2. Search Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Display Employees")
        print("6. List Operations")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            search_employee()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            display_employees()
        elif choice == '6':
            list_operations_menu()
        elif choice == '7':
            print("Thank you for using the Employee Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

def list_operations_menu():
    while True:
        print("List Operations")
        print("1. Sort employees by name")
        print("2. Sort employees by age")
        print("3. Sort employees by position")
        print("4. Back to Main Menu")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            sort_employees_by_name()
        elif choice == '2':
            sort_employees_by_age()
        elif choice == '3':
            sort_employees_by_position()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def sort_employees_by_name():
    sorted_employees = sorted(employees, key=lambda x: x['name'])
    print("Sorted Employees by Name:")
    for employee in sorted_employees:
        print_employee_details(employee)

def sort_employees_by_age():
    sorted_employees = sorted(employees, key=lambda x: x['age'])
    print("Sorted Employees by Age:")
    for employee in sorted_employees:
        print_employee_details(employee)

def sort_employees_by_position():
    sorted_employees = sorted(employees, key=lambda x: x['position'])
    print("Sorted Employees by Position:")
    for employee in sorted_employees:
        print_employee_details(employee)

# Run the program
main_menu()
