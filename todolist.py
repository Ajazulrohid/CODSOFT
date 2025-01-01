class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = new_task

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def view_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")

def main():
    todo_list = ToDoList()
    while True:
        print("\n1. Add Task\n2. Update Task\n3. Delete Task\n4. View Tasks\n5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
            index = int(input("Enter task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(index, new_task)
        elif choice == '3':
            todo_list.view_tasks()
            index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '4':
            todo_list.view_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
