task=[]
completed=[]
def add_task(n):
    task.append({"task":n,"done":False})
    print(f" '{n}'added to your to-do list")
def remove_task(index):
    if 1<=index <=len(task):
        removed=task.pop(index-1)
        print(f"task'{removed}' is removed from your to-do list")
    else:
        print("Invalid task number.Enter a valid task number")
def display_task(task):
    if task:
        print("to-do list")
        for j, task_info in enumerate(task,start=1):
            status="(done)" if task_info ["done"] else "(not done)"
            print(f"{j}. {task_info['task']} {status}")
    else:
        print("your to-do list is empty")
def mark_completed(index):
    if 1<=index<=len(task):
        task[index-1]["done"]=True
        print(f"task '{task[index-1]['task']}' is marked as completed")
    else:
        print("invalid.please enter a valid task")
while True:
    print("--options--")
    print("1. Display to-do list")
    print("2. Add a task")
    print("3. mark a task as completed")
    print("4. remove a task")
    print("5. exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        display_task(task)
    elif choice==2:
        n=input("enter a task:")
        add_task(n)
    elif choice==3:
        index=int(input("enter the task number to be completed as mark:"))
        mark_completed(index)
    elif choice==4:
        display_task(task)
        index=int(input("enter a task  number to be removed:"))
        remove_task(index)
    elif choice==5:
        print("exiting....!")
        break
    else:
        print("inavlid choice.please enter a valid choice")

