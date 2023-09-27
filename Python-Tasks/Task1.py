# To-do list Application

# Initialize an empty list to store tasks
toDoList = []


# Function to add a task to the list
def addTask():
    print("Excellent! Let's create a new task.")
    newTask = input('Please provide a description for the task:')
    toDoList.append(newTask)
    print("Task added successfully!")


# Function to update a task
def updateTask():
    if not toDoList:
        print("Your to-do list is empty. Add some tasks first.")
    else:
        print("Here is your current to-do list:")
        displayTasks()
        taskIndex = getTaskIndex()
        if taskIndex is not None:
            newTask = input('Enter the updated task: ')
            toDoList[taskIndex] = newTask
            print('Task updated successfully!')


# Function to delete a task
def deleteTask():
    if not toDoList:
        print("Your to-do list is empty. First add some task.")
    else:
        print("That\'s your current to-do list:")
        displayTasks()
        taskIndex = getTaskIndex()
        if taskIndex is not None:
            deletedTask = toDoList.pop(taskIndex)
            print(f'Task "{deletedTask}" deleted successfully!')


# Function to display tasks
def displayTasks():
    if not toDoList:
        print("Oops! The task list is empty. Add some tasks first.")
    else:
        for index, task in enumerate(toDoList, start=1):
            print(f"{index}. {task}")


# Function to get the task index from the user
def getTaskIndex():
    try:
        taskIndex = int(input('Please input the task index: ')) - 1
        if 0 <= taskIndex < len(toDoList):
            return taskIndex
        else:
            print('Invalid index. Your Task isn\'t not updated/deleted.')
    except ValueError:
        print('Invalid input. Please enter a valid number.')


# Main loop
while True:
    print('\n--- TO-DO LIST APPLICATION ---')
    print('1. Add a New Task')
    print('2. Update Task')
    print('3. Delete Task')
    print('4. View Task List')
    print('5. Exit')

    choice = input('Enter the number for the option to be chosen : ')

    if choice == '1':
        addTask()
    elif choice == '2':
        updateTask()
    elif choice == '3':
        deleteTask()
    elif choice == '4':
        displayTasks()
    elif choice == '5':
        print('Thanks for using To-Do List. Goodbye!')
        break
    else:
        print('Oops! That\'s an invalid choice. Please select a valid option.')
