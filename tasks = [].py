tasks = []

def new_task(): 
    id_task=int(input("ENTER ID "))
    name_task=input("ENTER NAME ")
    description_task=input("ENTER DESCRIPTION ")
    priority_task=input("ENTER PRIORITY ")
    status_task=input("ENTER STATUS ")

    tasks.append({
        "ID":int(id_task),
        "NAME":str(name_task),
        "DESCRIPTION":str(description_task),
        "PRIORITY":str(priority_task),
        "STATUS":str(status_task)})
    
    print("REGISTERED TASK")


def check_task():
    if not tasks:
        print("NO TASK") #WE VERIFY THAT INFORMATION EXISTS
    else:
        print("\n ====TASK_LIST==== ")

        for t in tasks:# WE ITERATE THROUGH THE LIST WITH A FOR LOOP
            print(f"ID: {t['ID']} | NAME: {t['NAME']} | DESCIPTION: {t['DESCRIPTION']} | PRIORITY: {t['PRIORITY']} | STATUS: {t['STATUS']} ")


def search_task():
    if not tasks:
        print("NO TASK")# WE VERIFY THAT INFORMATION EXISTS

    else:
        search = input("ENTER ID")
        found = False 

        for s in tasks:# WE ITERATE THROUGH THE LIST WITH A FOR LOOP
            if s["NAME"]==search:
                found=True 
                break # WE BREAK THE LOOP WHEN IT IS TRUE

            print(f"ID: {s['ID']} | NAME: {s['NAME']} | DESCIPTION: {s['DESCRIPTION']} | PRIORITY: {s['PRIORITY']} | STATUS: {s['STATUS']} ")
def update_task():
    if not tasks:
        print("NO TASK ") # WE VERIFY THAT INFORMATION EXISTS
    else:
        updata=int(input("ENTER ID "))
        found=False
        for u in tasks:
            u["ID"]==updata
            u["NAME"]=input("UPDATE NAME" )
            u["DESCRIPTION"]=input("UPDATE DESCRIPTION ")
            u["PRIORIY"]=input("UPDATE PRIORITY ")
            u["STATUS"]=input("UPDATE STATUS ")
            found = True
            break

def delete_task():
    if not tasks:
        print("NO TASK ")
    else:
        delete=int(input("ENTER ID "))

        for d in tasks:
            tasks.remove()
            found = True
            print("THE TASK WAS DELETED")


while True:

    # HERE WE PRINT THE VISUALS OF THE OPTIONS MENU
    
    print ("""===System_Managment===
           1.New task
           2.Check task
           3.Search 
           4.Update task
           5.Delete task


        """)
# WE CHOOSE OPTION
    option = int(input("ENTER VALID OPTION "))

# WE CHOOSE OPTION 1 AND REGISTER THE TASK BY ENTERING THE REQUIRED DATA
    
    if option == 1:
       new_task()
# WE CHOOSE OPTION 2 TO VIEW THE LIST OF CURRENT TASKS       
    elif option == 2:
       check_task()

# WE CHOOSE OPTION 3 TO SEARCH THE ESPECIFIT TASK    
      
    elif option == 3:
       search_task()

# WE CHOOSE OPTION 4 TO UPDATE  

    elif option == 4:
       update_task()

# WE CHOOSE OPTION 5 TO DELETE A TASK

    elif option == 5:
       delete_task()

# IF YOU ENTER AN INVALID OPTION, WE WILL DISPLAY AN ERROR AND ASK YOU TO ENTER A VALID ONE.
    
    else:
        print("ERROR, ENTER VALID OPTION ")