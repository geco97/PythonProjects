import datetime

class ToDoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name, category, due_date, priority):
        """Add a new task to the list."""
        task = {
            "name": task_name,
            "category": category,
            "due_date": datetime.datetime.strptime(due_date, "%Y-%m-%d"),
            "priority": priority,
            "completed": False
        }
        self.tasks.append(task)
        print(f"Task '{task_name}' added successfully!")

    def view_tasks(self, filter_by=None):
        """View all tasks or filter them by category or priority."""
        if not self.tasks:
            print("No tasks available.")
            return

        print("\nYour Tasks:")
        for task in self.tasks:
            if filter_by == "category" and task["category"].lower() != filter_value.lower():
                continue
            if filter_by == "priority" and task["priority"].lower() != filter_value.lower():
                continue

            status = "Completed" if task["completed"] else "Pending"
            print(f"- {task['name']} (Category: {task['category']}, Due: {task['due_date'].date()}, Priority: {task['priority']}, Status: {status})")

    def mark_as_complete(self, task_name):
        """Mark a specific task as completed."""
        for task in self.tasks:
            if task["name"].lower() == task_name.lower() and not task["completed"]:
                task["completed"] = True
                print(f"Task '{task_name}' marked as complete.")
                return
        print(f"Task '{task_name}' not found or already completed.")

    def remove_task(self, task_name):
        """Remove a task from the list."""
        for task in self.tasks:
            if task["name"].lower() == task_name.lower():
                self.tasks.remove(task)
                print(f"Task '{task_name}' removed successfully.")
                return
        print(f"Task '{task_name}' not found.")

    def suggest_overdue_tasks(self):
        """Suggest tasks that are overdue."""
        today = datetime.datetime.now()
        overdue_tasks = [task for task in self.tasks if task["due_date"] < today and not task["completed"]]

        if not overdue_tasks:
            print("No overdue tasks. Great job staying on track!")
        else:
            print("\nOverdue Tasks:")
            for task in overdue_tasks:
                print(f"- {task['name']} (Due: {task['due_date'].date()})")

# Main Program
def main():
    app = ToDoApp()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Remove Task")
        print("5. Suggest Overdue Tasks")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter task name: ")
            category = input("Enter category (e.g., Work, Personal): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority (High, Medium, Low): ")
            app.add_task(name, category, due_date, priority)

        elif choice == "2":
            filter_option = input("Filter tasks by (none/category/priority): ").lower()
            filter_value = None
            if filter_option in ["category", "priority"]:
                filter_value = input(f"Enter {filter_option} value: ")
            app.view_tasks(filter_by=filter_option)

        elif choice == "3":
            name = input("Enter task name to mark as complete: ")
            app.mark_as_complete(name)

        elif choice == "4":
            name = input("Enter task name to remove: ")
            app.remove_task(name)

        elif choice == "5":
            app.suggest_overdue_tasks()

        elif choice == "6":
            print("Goodbye! Stay productive!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
