import csv, json
class Task:
    def __init__(self, ID, title, description, status):
        self.ID=ID
        self.title=title
        self.description=description
        self.status=status
    def to_list(self):
        return [self.ID, self.title, self.description, self.status]
    
    def to_dict(self):
        return {"Task ID":self.ID,"Task title":self.title,"Task Description":self.description,"Task Status":self.status}

class Storage:
    def __init__(self, filename):
        self.filename=filename
    
    def save(self,tasks):
        pass

    def load(self):
        pass

class JSONStorage(Storage):
    def save(self, tasks):
        with open(self.filename, "w") as file:
            json.dump([Task(*(data for data in task)).to_dict() for task in tasks], file, indent=2)
    

    def load(self):
        try:
            with open(self.filename, "r") as file:
                return [Task(*task_data.values()).to_list() for task_data in json.load(file)]
        except FileNotFoundError:
            return []

class CSVStorage(Storage):
    def save(self, tasks):
        with open(self.filename, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Task ID", "Task Title", "Task Description", "Task Status"])
            for task in tasks:
                writer.writerow(task)

    def load(self):
        try:
            with open(self.filename, "r") as file:
                reader = csv.reader(file)
                next(reader)
                return [Task(*row).to_list() for row in reader]
        except FileNotFoundError:
            return []

class ToDoManager:
    def __init__(self, storage: Storage):
        self.storage = storage
        self.tasks = []
    
    def add_task(self):
        id = int(input("Enter Task ID: "))
        while(self.id_exists(id=id)):
            id = int(input("This task ID is already in use. Please enter another task ID: "))
        title = input("Enter title: ")
        description = input("Enter task description: ")
        status = input("Enter task status: ")
        task_to_add = Task(ID=id, title=title, description=description, status=status)
        self.tasks.append(task_to_add.to_list())
        print("Task added!")

    def id_exists(self, id):
        for task in self.tasks:
            if id==task[0]: return True
        return False

    def view_tasks(self):
        for task in self.tasks:
            print(', '.join(list(str(a) for a in task)))

    def update_task(self):
        id = int(input("Enter task ID: "))
        up_title = input("Enter new task title: ")
        up_description = input("Enter new task description: ")
        up_status = input("Enter new task status: ")
        for task in self.tasks:
            if task[0]==id:
                task[1]=up_title
                task[2]=up_description
                task[3]=up_status
        print("Task updated!")

    def delete_task(self):
        id = int(input("Enter task ID to delete: "))
        while(not self.id_exists(id=id)):
            id = int(input("Task with such ID does not exist! Please enter an existing task ID: "))
        for task in self.tasks:
            if task[0]==id:
                self.tasks.remove(task)

        print("Task deleted!")

    def filter_tasks(self):
        self.tasks.sort(key=lambda x: x[3])
        print("Tasks are filtered!")

    def save_tasks(self):
        self.storage.save(self.tasks)
        print("Tasks are saved!")

    def load_tasks(self):
        for row in self.storage.load():
            print(", ".join(list(str(a) for a in row)))
        print("Tasks are loaded!")

def main():
    print("Welcome to the To-Do Application!")
    print("1. Add a new task\n\
2. View all tasks\n\
3. Update a task\n\
4. Delete a task\n\
5. Filter tasks by status\n\
6. Save tasks\n\
7. Load tasks\n\
8. Exit")
    option = int(input("Enter your choice: "))
    admin = ToDoManager(JSONStorage("todo_list.json"))
    while(option<8):
        if option==1: admin.add_task()
        if option==2: admin.view_tasks()
        if option==3: admin.update_task()
        if option==4: admin.delete_task()
        if option==5: admin.filter_tasks()
        if option==6: admin.save_tasks()
        if option==7: admin.load_tasks()
        option = int(input("Enter your choice: "))
    print("Goodbye!")

with open("todo_list.json", "w") as file:
    pass
with open("todo_list.csv", "w") as file:
    pass

main()