Command Line Task Manager

Fancy task managers with slick user interfaces are slow and cumbersome. Now that you have the power of the command line at your disposal, you would like be able to access all your tasks without having to burden yourself with tedious pointing and clicking. For your final project, you will design an object oriented task manager application that will allow you to enter tasks, save them to a file, and retrieve them...all without moving your hands from the keyboard.

 
Data Objects

The program should implement the following class types:

 
Task Class

Each task should be able to be uniquely identified from all other tasks by a numeric identifier. Tasks should be assigned a priority level of 1, 2 or 3 to indicate the importance (3 is the highest priority).

A Task object should store the date they were created and completed. In addition, the task manager should allows for different types of tasks: a task with no due date and a task with a due date.

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
    pass

 
Tasks Class

Implement a Tasks objects that will contain all the Task objects. Tasks should be implemented as a list of Task objects. You may use the standard Python list() to hold you Task objects. The list should be ordered by the creation date (to improve search efficiency). While running, you program should only have a single instance of Tasks.

class Tasks:
   """A list of `Task` objects."""
   
    def __init__(self):
        """Read pickled tasks file into a list"""
        # List of Task objects
        self.tasks = [] 
        # your code here

    def pickle_tasks(self):
        """Picle your task list to a file"""
        # your code here

    # Complete the rest of the methods, change the method definitions as needed
    def list(self):
        pass

    def report(self):
        pass

    def done(self):
        pass

    def query(self):
        pass

    def add(self):
        pass


You will need to implement all the methods that support the add, delete, list, report, query and done commands described below.

 
Data

All the Tasks data should be serialized to disk using Python pickle module. Write to a file named .todo.pickle in the same directory as your program. The . is not a typo. Prefixing a file with a . makes it an invisible file.

    This file will exist in a directory, but will not be visible to the user by default. This is a good practice when storing data in a file that you do not want the user to open or modify. See unix challenge on how to visualize invisible files.

When your program exits, you should ensure that all tasks have been serialized to disk. When you program begins, you should ensure that all your tasks are loaded into objects from the serialized file.

 
Running the Program

The user should run the program completely from the command line passing in commands and arguments that will alter the behavior of the program. The commands are --add, --delete, --list, --report, --query, and --done. Use the argparse package to help with parsing the command line arguements.

Each command will be followed with arguments, as seen in the following examples:

 
Task Add

Add a new task by using the --add command. Examples of adding tasks are shown below.

Note that the task description needs to be enclosed in quotes if there are mulitple words. argparse should provide sufficient error handling for user input, however you need to test that the data matches the type expected.

The unique identifier is returned when the operation is successful. If the operation is not successful, inform the user and end the program. Remember that the due date is optional. If a priority is not given, then assign it a default value of 1.

$ python todo.py --add "Walk Dog" --due 4/17/2018 --priority 1
Created task 1

$ python todo.py --add 2 --due 4/17/2018 --priority 1
There was an error in creating your task. Run "todo -h" for usage instructions.

$ python todo.py --add "Study for finals" --due 3/20/2018 --priority 3
Created task 2

$ python todo.py --add "Buy milk and eggs" —due friday --priority 2
Created task 3

$ python todo.py --add "Cook eggs"
Created task 4

 
Task List Command

Use the --list command to display a list of the not completed tasks sorted by the due date. If tasks have the same due date, sort by decreasing priority (1 is the highest priority). If tasks have no due date, then sort by decreasing priority.

Note that only tasks that are not completed should be listed with this command. The Age in the table is the number of days since the task was created.

Follow the formatting shown below.

$ python todo.py list

ID   Age  Due Date   Priority   Task
--   ---  --------   --------   ----
1    3d   4/17/2018   1         Walk dog
2    10d  3/20/2018   3         Study for finals
3    1d   -           1         Buy eggs
4    30d  -           2         Make eggs

 
Task List Command Using a Query Term

Search for tasks that match a search term using the --query command. Only return tasks are not completed in your results.

$ python todo.py --query eggs

ID   Age  Due Date   Priority   Task
--   ---  --------   --------   ----
3    1d   -           2         Buy eggs
4    30d  -           1         Make eggs

Muliple terms should be able to be searched. The argparse package allows you to pass in multiple values for a single argument using nargs='+':

parser.add_argument('--query', type=str, required=False, nargs="+", help="priority of task; default value is 1")

For example:

$ python todo.py --query eggs dog

ID   Age  Due Date   Priority   Task
--   ---  --------   --------   ----
1    3d   4/17/2018   1         Walk dog
3    1d   -           2         Buy eggs
4    30d  -           1         Make eggs

 
Task Done Command

Complete a task by passing the done argument and the unique identifier. The following example complete tasks 1 and 2. Remember that you are not deleting a task, you are just marking it as complete. Your --list methods should ensure that it not longer is printed to the terminal.

$ python todo.py --done 1
Completed task 1

$ python todo.py --done 2
Completed task 2

$ python todo.py --list

ID   Age  Due Date   Priority   Task
--   ---  --------   --------   ----
3    1d   -           2         Buy eggs
4    30d  -           1         Make eggs

 
Delete Command

Delete a task by passing the --delete command and the unique identifier.

$ python todo.py --delete 3
Deleted task 3

$ python todo.py list

ID   Age  Due Date   Priority   Task
--   ---  --------   --------   ----
4    30d  -           1         Make eggs

 
Task Report Command

List all tasks, including both completed and incomplete tasks, using the report command. Follow the formatting shown below for the the output. Follow the same reporting order as the --list command.

$ python todo.py report

ID   Age  Due Date   Priority   Task                Created                       Completed
--   ---  --------   --------   ----                ---------------------------   -------------------------
1    3d   4/17/2018   1         Walk dog            Mon Mar  5 12:10:08 CST 2018  Mon Mar  5 12:10:08 CST 2018
2    10d  3/20/2018   3         Study for finals    Tue Mar  6 12:10:08 CST 2018  Tue Mar  6 12:10:08 CST 2018
3    1d   -           2         Buy eggs            Tue Mar  6 12:10:08 CST 2018  -
4    30d  -           1         Make eggs           Tue Mar  6 12:10:08 CST 2018  -

    Note: This action will be useful for debugging and testing the completed and deleted commands.

 
Overall Notes

This assignment is your opportunity to utilized everything you have learned this quarter into a fully functioning application. You should consider all the techniques available to you that are needed to implement the required functionality.

At each stage of development, you should be making careful evaluations of your implementation details. For example:

    How will your organize your code?
    How structure your application flow?
    How will you sort data? At what stage?
    What search approach will you use?
    How will you represent date stamps?

Consider how you will balance best practices, efficiency and ease of implementation in this assignment. We will be looking for implementations that make best use of object oriented programming practices and make justifiable decisions about algorithm choices. Please use comments and docstring throughout. We will be reading your code as developers and executing it as users.
