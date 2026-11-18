from task_manager import TaskManager

def show(manager):
    tasks = manager.list_tasks()
    if not tasks:
        print("No tasks yet.")
    for t in tasks:
        mark = "x" if t["completed"] else " "
        print(f'{t["id"]}. [{mark}] {t["title"]}')

def main():
    manager = TaskManager()
    while True:
        print("\n1. Add  2. Show  3. Mark complete  4. Delete  5. Exit")
        choice = input("Choose: ").strip()
        try:
            if choice == "1":
                manager.add_task(input("Title: "))
            elif choice == "2":
                show(manager)
            elif choice == "3":
                manager.complete_task(int(input("Task id: ")))
            elif choice == "4":
                manager.delete_task(int(input("Task id: ")))
            elif choice == "5":
                break
            else:
                print("Invalid choice.")
        except (ValueError, KeyError) as e:
            print("Oops:", e)
        except NotImplementedError:
            print("Not implemented yet.")

if __name__ == "__main__":
    main()