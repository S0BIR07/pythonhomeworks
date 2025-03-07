import os
import json
import csv

class Manager:
    def __init__(self):
        self.tasks = []
        self.id = (x for x in range(1,1001))
    def add_task(self, values: list):
        self.tasks.append({"id":next(self.id), "task": values[0], "completed":values[1], "priority": values[2]})
    def edit_task(self, id: int, values: list):
        for task in self.tasks:
            if(list(task.values())[0]==id):
                task["task"]=values[0]
                task["completed"] = values[1]
                task["priority"] = values[2]
                print("Task is modified successfully!")
                return
        else: print("Task with such ID not found!")
    # saves tasks in json file
    def save_tasks(self):
        if self.tasks==[]:
            print("You have no temporary tasks yet!")
            return
        with open("tasks.json", "a") as file:
            json.dump(self.tasks, file, indent=2)
        print("Tasks are saved successfully!")
        self.tasks = [] # cleares the temporary tasks after saving in file to prevent the overwriting of tasks 
    def load_tasks(self):
        if os.path.getsize("tasks.json")==0:
            print("There is no available tasks in the file yet!")
            return
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        print("ID, Task name, Completed, Priority")
        for task in tasks:
            print(f"{list(task.values())[0]}, {list(task.values())[1]}, {list(task.values())[2]}, {list(task.values())[3]}")
    def display(self):
        if self.tasks == []:
            print("You have no temporary tasks yet")
            return
        print("ID, Task name, Completed, Priority")
        for task in self.tasks:
            print(f"{list(task.values())[0]}, {list(task.values())[1]}, {list(task.values())[2]}, {list(task.values())[3]}")
    def stats(self):
        if self.tasks==[]:
            print("There is no available temporary tasks yet!")
            return
        total_tasks = len(self.tasks)
        completed_tasks = len([task for task in self.tasks if list(task.values())[2]==True])
        average_priority = round(sum([list(x.values())[3] for x in self.tasks])/total_tasks, 2)
        print(f"Total tasks: {total_tasks}")
        print(f"Completed tasks: {completed_tasks}")
        print(f"Pending tasks: {total_tasks-completed_tasks}")
        print(f"Average priority: {average_priority}")
    def convert_to_csv(self):
        if os.path.getsize("tasks.json")==0:
            print("There is no available tasks in the file yet!")
            return
        with open("tasks.json", "r") as file:
            tasks = json.load(file)                # reads data from .json file
        csv_format = []          # empty list to append data from tasks
        for task in tasks:
            csv_format.append(list(task.values()))     # append data to the empty list
        with open("tasks.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow(['ID','Task','Completed','Priority']) # write the header
            writer.writerows(csv_format)  # append the list to the .csv file

def main():
    admin = Manager()
    with open("tasks.json", "w") as file: # creates an empty .json file for appending
        pass
    with open("tasks.csv", "w") as file: # creates an empty .csv file for appending
        pass
    print("Option 1: Add new task \n\
Option 2: Edit task \n\
Option 3: Save tasks to file \n\
Option 4: Load existing tasks in the file \n\
Option 5: Display tasks \n\
Option 6: Show task completion stats \n\
Option 7: Convert to CSV \n\
Option 8: Exit")
    option = int(input("Choose an option: "))
    while option<8:
        if option==1:
            task = input("Task name: ")
            completed = bool(input("Completed? Enter anything if yes. Or just press Enter button if no: "))
            priority = int(input("Priority (in a scale of 1-3): "))
            while (priority!=1 and priority!=2 and priority!=3):
                priority = int(input("Priority needs to be in a scale of 1-3: "))
            admin.add_task([task,completed,priority])
        elif option==2:
            id = int(input("Enter task ID: "))
            task = input("New task name: ")
            completed = bool(input("New completed status (Enter anything if yes, or just press Enter button if no): "))
            priority = int(input("New priority (in a scale of 1-3): "))
            while (priority!=1 and priority!=2 and priority!=3):
                priority = int(input("Priority needs to be in a scale of 1-3: "))
            admin.edit_task(id=id,values=[task,completed,priority])
        elif option==3:
            admin.save_tasks()
        elif option==4:
            admin.load_tasks()
        elif option==5:
            admin.display()
        elif option==6:
            admin.stats()
        elif option==7:
            admin.convert_to_csv()
        print("Option 1: Add new task \n\
Option 2: Edit task \n\
Option 3: Save tasks to file \n\
Option 4: Load existing tasks in the file \n\
Option 5: Display tasks \n\
Option 6: Show task completion stats \n\
Option 7: Convert to CSV \n\
Option 8: Exit")
        option=int(input("Choose an option: "))
    print("Goodbye!")
if (__name__=="__main__"):
    main()