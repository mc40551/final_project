import argparse
import pickle
import time
from datetime import datetime

class Task:
    """Representation of a task

    Attributes:
    - created - date
    - completed - date
    - name - string
    - unique id - number
    - priority - int value of 1, 2, or 3; 1 is default
    - due date - date, this is optional
    """
    def __init__(self, name, unique_id=None, due_date=None, priority=1):
        self.created = time.strftime("%a %b %d %H:%M:%S CST %Y")
        self.completed = None
        self.unique_id = unique_id
        self.name = name
        # format the due date
        self.due_date = (
            datetime.strptime(due_date, "%m/%d/%Y").strftime("%m/%d/%Y")
            if due_date
            else None
        )
        self.priority = priority

class Tasks:
    """A list of `Task` objects."""
    def __init__(self):
        """Read pickled tasks file into a list"""
        self.tasks = [] 
        self.load_tasks()

    def load_tasks(self):
        # load list of tasks
        try:
            with open('.todo.pickle', 'rb') as f:
                self.tasks = pickle.load(f)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        # save list of tasks
        with open('.todo.pickle', 'wb') as f:
            pickle.dump(self.tasks, f)

    def list(self):
        # create a list of incomplete tasks and sort the list by due date and priority
        incomplete_tasks = [task for task in self.tasks if task.completed is None]
        sorted_tasks = sorted(incomplete_tasks, key=lambda x: (x.due_date is None, x.due_date, -x.priority))
        # print the list
        print(f"ID\tAge\tDue Date\tPriority\tTask\n--\t---\t--------\t--------\t----")
        for i in sorted_tasks:
            age = (datetime.now() - datetime.strptime(i.created, "%a %b %d %H:%M:%S CST %Y")).days
            due_date = i.due_date if i.due_date else "-"
            print(f"{i.unique_id}\t{age}\t{i.due_date}\t{i.priority}\t{i.name}")

    def report(self):
        # report all tasks
        sorted_tasks = sorted(self.tasks, key=lambda x: (x.due_date is None, x.due_date, -x.priority))
        print(f"ID\tAge\tDue Date\tPriority\tTask\tCreated\tCompleted\n--\t---\t--------\t--------\t----\t---------------------------\t-------------------------")
        for i in sorted_tasks:
            age = (datetime.now() - datetime.strptime(i.created, "%a %b %d %H:%M:%S CST %Y")).days
            completed = i.completed if i.completed else "-"
            due_date = i.due_date if i.due_date else "-"
            print(f"{i.unique_id}\t{age}\t{i.due_date}\t{i.priority}\t{i.name}\t{i.created}\t{completed}")

    def done(self, id):
        # mark a task as complete
        id = int(id)
        for task in self.tasks:
            if task.unique_id == id:
                task.completed = time.strftime("%a %b %d %H:%M:%S CST %Y")
                self.save_tasks()
                print(f"Completed task {id}")
                return
        print(f"No task found with ID {id}")

    def query(self, keywords):
        # iterate through each keyword by each task
        matching_tasks = []
        for task in self.tasks:
            if task.completed is None:
                for keyword in keywords:
                    if keyword.lower() in task.name.lower():
                        matching_tasks.append(task)
                        break
        
        sorted_tasks = sorted(matching_tasks, key=lambda x: (x.due_date is None, x.due_date, -x.priority))
        
        print(f"ID\tAge\tDue Date\tPriority\tTask\n--\t---\t--------\t--------\t----")
        for i in sorted_tasks:
            age = (datetime.now() - datetime.strptime(i.created, "%a %b %d %H:%M:%S CST %Y")).days
            due_date = i.due_date if i.due_date else "-"
            print(f"{i.unique_id}\t{age}\t{i.due_date}\t{i.priority}\t{i.name}")

    def add(self, task):
        # generate an id for each task and append the task to the list
        task.unique_id = len(self.tasks) + 1
        self.tasks.append(task)
        self.save_tasks()
        print(f"Created task {task.unique_id}")

    def delete(self, id):
        # check id and delete the task
        id = int(id)
        for i, task in enumerate(self.tasks):
            if task.unique_id == id:
                del self.tasks[i]
                self.save_tasks()
                print(f"Deleted task {id}")
                return
        print(f"No task found with ID {id}")

def parse_input():
    # use argparse to parse commend line input
    parser = argparse.ArgumentParser(description="Command-line Task Manager")
    
    # define commands
    commands = parser.add_mutually_exclusive_group(required=True)
    commands.add_argument('--add', action='store_true', help="Add a new task")
    commands.add_argument('--list', action='store_true', help="List all tasks")
    commands.add_argument('--query', nargs='+', help="Search tasks by keywords")
    commands.add_argument('--done', type=str, help="Mark a task as completed by ID")
    commands.add_argument('--delete', type=str, help="Delete a task by ID")
    commands.add_argument('--report', action='store_true', help="Generate a report of all tasks")

    # required and optional arguments
    parser.add_argument('task_description', nargs='*', help="Task description for add command")
    parser.add_argument('--due', type=str, help="Due date for the task")
    parser.add_argument('--priority', type=int, choices=[1, 2, 3], default=1, help="Priority of task (1-3)")

    return parser.parse_args()

def main():
    # assign the input and parse it
    args = parse_input()
    tasks = Tasks()

    # check the command
    if args.add:
        try:
            new_task = Task(" ".join(args.task_description), due_date=args.due, priority=args.priority)
            tasks.add(new_task)
        except Exception as e:
            print(f"Error adding task: {e}")
    elif args.list:
        tasks.list()
    elif args.query:
        tasks.query(args.query)
    elif args.done:
        tasks.done(args.done)
    elif args.delete:
        tasks.delete(args.delete)
    elif args.report:
        tasks.report()


if __name__ == "__main__":
    main()
