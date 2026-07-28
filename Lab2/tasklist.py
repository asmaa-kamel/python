tasks=[]

def add_task():
    newTask=input("Enter New task :")
    tasks.append(newTask)
    print("Task added successfully!!")
    
def view_tasks():
    if not tasks: 
        print('No Tasks Found!') 
        return
    print("These are your Tasks: ") 
     
    for i, task in enumerate(tasks, start=1): 
        print(f"{i}- [{task}]")   
        
def update_task():
    indx=int(input("Enter the number of the task you want to edit :"))
    update=input("Enter the edited task :")
    tasks[indx-1]=update
    print("Task edites successfully!!!")
    
def done_task():
    indx=int(input("Enter the number of the task you've done :"))
    tdone= tasks[indx-1]+"done ✅✅"
    tasks[indx-1]=tdone
    print("Congrats on doing the task!!!")
        
def del_task():
    indx=int(input("Enter the number of the task you want to delete :"))
    tasks.pop(indx-1)
    print("Task deleted successfully!!")
            




while True:
    choice=input("""1)Add task
          2)View tasks
          3)Update task
          4)mark task done task
          5)Delete task
          6)exit 
          Choose your operation:""")
    if choice=="1":
         add_task()
        
    elif choice=="2":
        view_tasks()
        
    elif choice=="3":
        update_task()
        
    elif choice=="4":
        done_task()
        
    elif choice=="5":
        del_task()    
        
        
    elif choice=="6":
        print("Ending program...")
        break        
    
    else:
        print("Enter valid operation.")        
        
    
    