with open("employee_records.txt", "w") as file:
    file.close()
def append_data(data):
    with open("employee_records.txt","a") as file:
        file.write(f"{data}, \n")
def display_records():
    with open("employee_records.txt", "r") as file:
        print("".join(file.readlines()))
def search_employee(id):
    with open("employee_records.txt", "r") as file:
        lines = file.readlines()
        for record in lines:
            if id==record.split(", ")[0]:
                print(record)
                return True
            else: 
                print("No such employee found")
                return False
def new_record():
    Name = input("Input the new employee name: ")
    Position = input("Input the new employee position: ")
    Salary = input("Input the new employee salary: ")
    return ", ".join([Name, Position, str(Salary)])
def update_record(id, data):
    if search_employee(id) == False: 
        print("No such employee found")
        return
    with open("employee_records.txt", "r") as file:
        lines = file.readlines()
    with open("employee_records.txt", "w") as file:
        for record in lines:
            if id==record.split(", ")[0]:
                file.write(f"{str(id)}, {data}")
            else: file.write(record)
def delete_record(id):
    if search_employee(id) == False:
        print("No such employee found")
        return
    with open("employee_records.txt", "r") as file:
        lines = file.readlines()
    with open("employee_records.txt", "w") as file:
        for record in lines:
            if id!=record.split(", ")[0]:
                file.write(record)
def record_data():
    try:
        Id = int(input("Input the new employee ID: "))
    except ValueError:
        Id = int(input("Please input an integer for the employee ID: "))
    Name = input("Input the new employee name: ")
    Position = input("Input the new employee position: ")
    try:
        Salary = int(input("Input the new employee salary: "))
    except ValueError:
        Salary = int(input("Please enter a positive integer: "))
    return ", ".join([str(Id), Name, Position, str(Salary)])
option = int(input("Choose an option: \n\
Option 1: Append a new employee record.\n\
Option 2: Display all employee records.\n\
Option 3: Search for an employee.\n\
Option 4: Update an employee’s information (name, position, or salary).\n\
Option 5: Delete an employees record from the file using the Employee ID.\n\
Option 6: Exit the program.\n"))
while(option!=6):
    if option==1:
        append_data(record_data())
    elif option==2:
        display_records()
    elif option==3:
        Id = input("Input the employee Id: ")
        search_employee(Id)
    elif option==4:
        Id = input("Input the employee Id: ")
        update_record(Id, new_record())
    elif option==5:
        Id = input("Input the employee Id: ")
        delete_record(Id)
    option = int(input("Choose another option: \n\
Option 1: Append a new employee record.\n\
Option 2: Display all employee records.\n\
Option 3: Search for an employee.\n\
Option 4: Update an employee’s information (name, position, or salary).\n\
Option 5: Delete an employees record from the file using the Employee ID.\n\
Option 6: Exit the program.\n"))