class Employee:
    def __init__(self, employee_id: int, name: str, position: str, salary: int):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
    
    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    def add(self, employee: Employee):
        if self.id_exists(employee.employee_id):
            print("Employee ID already exists. Please use a different ID.")
            return
        with open("employees.txt", "a") as file:
            file.write(f"{employee}\n")
        print("Employee added successfully!")

    def view(self):
        with open("employees.txt", "r") as file:
            print(file.read())

    def search(self, employee_id):
        with open("employees.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if str(employee_id) == line.split(", ")[0]:
                    return line
            raise ValueError("Employee with such ID is not found!")

    def update(self, employee_id, new_info):
        with open("employees.txt", "r") as file:
            lines = file.readlines()
        with open("employees.txt", "w") as file:
            for line in lines:
                if str(employee_id) != line.split(", ")[0]:
                    file.write(line)
                else:
                    file.write(f"{employee_id}, {new_info}\n")
        print("Employee information updated successfully!")

    def delete(self, employee_id):
        with open("employees.txt", "r") as file:
            lines = file.readlines()
        with open("employees.txt", "w") as file:
            for line in lines:
                if str(employee_id) != line.split(", ")[0]:
                    file.write(line)
        print("Employee deleted successfully!")

    def id_exists(self, employee_id):
        with open("employees.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if str(employee_id) == line.split(", ")[0]:
                    return True
        return False

with open("employees.txt", "w") as file:
    pass

print("Welcome to the Employee Records Manager!\n\
1. Add new employee record\n\
2. View all employee records\n\
3. Search for an employee by Employee ID\n\
4. Update an employee's information\n\
5. Delete an employee record\n\
6. Exit")

option = int(input("Enter your choice: "))
admin = EmployeeManager()

while option != 6:
    if option == 1:
        id = int(input("Enter employee ID: "))
        while admin.id_exists(id):
            id = int(input("ID already exists. Try another ID: "))
        name = input("Employee name: ")
        position = input("Employee Position: ")
        try:
            salary = int(input("Employee Salary: "))
        except ValueError:
            print("Invalid type for employee salary!")
            salary = int(input("Enter Salary again: "))
        admin.add(Employee(employee_id=id, name=name, position=position, salary=salary))
    elif option == 2:
        admin.view()
    elif option == 3:
        try:
            id = int(input("Enter employee ID: "))
        except ValueError:
            print("Invalid type for employee ID!")
            id = int(input("Enter employee ID again: "))
        try:
            print(admin.search(employee_id=id))
        except ValueError as e:
            print(e)
    elif option == 4:
        try:
            id = int(input("Enter employee ID: "))
        except ValueError:
            print("Invalid type for employee ID!")
            id = int(input("Enter employee ID again: "))
        name = input("New employee name: ")
        position = input("New employee Position: ")
        try:
            salary = int(input("New employee Salary: "))
        except ValueError:
            print("Invalid type for employee salary!")
            salary = int(input("Enter Salary again: "))
        new_info = f"{name}, {position}, {salary}"
        admin.update(employee_id=id, new_info=new_info)
    elif option == 5:
        try:
            id = int(input("Enter employee ID: "))
        except ValueError:
            print("Invalid type for employee ID!")
            id = int(input("Enter employee ID again: "))
        if not admin.id_exists(id):
            print("No employee with such id")
        else:
            admin.delete(id)
    option = int(input("Enter your choice: "))
print("Goodbye!")