class Taskmanager :
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
        print("task is successfully")
    def show_tasks(self):
        if not self.tasks:
            print("no tasks")
        else:
            print("tasks:")
            for i, task in enumerate(self.tasks,1):
                print(f"{i}.{task}")
    def delete_task(self , task_number):
        if 0< task_number <=len (self.tasks):
            removed_task= self.tasks.pop(task_number-1)
            print(f"deleted task:{removed_task}")
        else:
            print("invalid task number")
        
manager = Taskmanager()
while True:
    try:
        print("\n1-Add task")
        print("2-Show tasks")
        print("3-Delete task")
        print("4-Exit")
        choice=int(input("Enter your choice:"))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue 

    if choice==1:
        task=input("Enter task :")
        manager.add_task(task)
    elif choice==2:
        manager.show_tasks()
    elif choice==3:
        try:
            task_number=int(input("Enter task number to delete:"))
            manager.delete_task(task_number)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice==4:
        print("Goodbye!")
        break
    else:
        print("invalid choice.")
