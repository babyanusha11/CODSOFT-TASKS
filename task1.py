class Task:
    def __init__(self, title, description='', completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title}: {self.description}"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description=''):
        task = Task(title, description)
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")

    def update_task(self, index, title=None, description=None):
        if 0 <= index < len(self.tasks):
            if title:
                self.tasks[index].title = title
            if description:
                self.tasks[index].description = description

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def mark_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.title}|{task.description}|{task.completed}\n")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    title, description, completed = line.strip().split('|')
                    task = Task(title, description, completed == 'True')
                    self.tasks.append(task)
        except FileNotFoundError:
            print("File not found.")


def main():
    todo_list = TodoList()
    todo_list.load_from_file('tasks.txt')

    while True:
        print("\nTo-Do List:")
        todo_list.view_tasks()
        print("\nOptions: add, update, delete, complete, save, load, exit")
        choice = input("Choose an option: ").strip().lower()

        if choice == 'add':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
        elif choice == 'update':
            index = int(input("Enter task number to update: ")) - 1
            title = input("Enter new title (leave blank to keep current): ")
            description = input("Enter new description (leave blank to keep current): ")
            todo_list.update_task(index, title if title else None, description if description else None)
        elif choice == 'delete':
            index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == 'complete':
            index = int(input("Enter task number to mark as complete: ")) - 1
            todo_list.mark_complete(index)
        elif choice == 'save':
            todo_list.save_to_file('tasks.txt')
        elif choice == 'load':
            todo_list.load_from_file('tasks.txt')
        elif choice == 'exit':
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()