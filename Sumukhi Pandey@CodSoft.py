# A To-Do List application is a useful project that helps users manage and organize their tasks efficiently. This project aims to create a
command-line or GUI-based application using Python, allowing users to create, update, and track their to-do lists.

toDoTasks =[]
print("Welcome to your to-do-list")
print("***************************")
userChoice=0
while userChoice !=4:
    print("Press 1 to view your to do list")
    print("Press 2 to add new task to your list")
    print("Press 3 to remove an existing task")
    print("Press 4 to exit")
    userChoice= int(input("Choose what do you want to do:"))
    if userChoice ==1:
        if len(toDoTasks)==0:
            print("Empty task list")
        else:
            for i in range(len(toDoTasks)):
                print(f"{i+1}: {toDoTasks[i]}")
        yesOrNo=input("Enter y to continue and n to exit: ") 
        if yesOrNo in ["n","N"]:
            userChoice=4
    elif userChoice==2:
        print("Enter the task in this format: ")
        task=input("Date/Time - Task")
        toDoTasks.append(task)
        yesOrNo=input("Enter y to continue and n to exit: ")
        if yesOrNo in["n","N"]:
            userChoice=4
    elif userChoice==3:
        print("Your current to do list looks like this:")
        if len(toDoTasks)==0:
            print("Empty task list")
        else:
            for i in range(len(toDoTasks)):
                 print(f"{i+1}:{toDoTasks[i]}")
        taskDelete=int(input("Enter the number written in front of the task you want to delete:"))
        toDoTasks.pop(taskDelete-1)
        print("1 task deleted")
        yesOrNo=input("Enter y to continue and n to exit: ")
        if yesOrNo in ["n","N"]:
            userChoice=4
            
            
