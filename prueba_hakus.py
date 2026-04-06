from funciones_prueba_hakus import(add_task,show_tasks,search_tasks,update_tasks,delete_task)


def main():
    task_list = []
    sw=True

# menu in which the user can interact and choose the desired option
    while sw is not False:
    
        print("\n--- MENU ---")
        print("1. register new tasks")
        print("2. check task list")
        print("3. search task")
        print("4. update tasks")
        print("5. delete task")
        print("6. leave")


# display options using print()
# The user is given a number to access a menu option; if they enter another number
# it will be marked as invalid and the system will ask again.


        option = input("Select an option ")

        if not option.isdigit() or int(option) < 1 or int(option) > 6:
            print("invalid option.")
            continue



# In option 1, the user is asked to enter the identifier, title, description, priority, and status of the task. 
# The system validates that the information entered by the user is correct to prevent the system from crashing.


        try:
            if option == "1":

                identifier_valid = False
                while not identifier_valid:
                    identifier = (input("enter the id "))
                    if identifier.isdigit():
                        identifier_valid = True
                
                    else:
                        print("Enter only numbers")

                    title = input("Enter the task title ").lower().strip()

                    description = input("Enter the task description ").lower().strip()

                    priority_valid = False
                    while not priority_valid:
                        priority = input("high, medium or low priority ").lower().strip()
                        if priority in ["high", "medium", "low"]:
                            priority_valid = True
                        else:
                            print("Enter 'high', 'medium',  'low'.")
                    

                    condition_valid = False
                    while not condition_valid:
                        condition = input("Enter the task status, complete or pending ")
                        if condition in ["complete", "pending"]:
                            condition_valid = True
                        else:
                            print("enter 'complete' or 'pending'. ")
                    
            

                    add_task(identifier,title,description,priority,condition,task_list)


            elif option == "2":
                show_tasks(task_list)



            elif option == "3":
                identifier = input("enter the task identifier ")
                result = search_tasks(task_list,identifier)
                print(result)


            elif option == "4":
                identifier = int(input("enter the task identifier "))
                title = input("enter the new title ")
                description = input("enter the new description ")
                priority = input("enter the new priority ")
                condition = input("enter the new condition ")
                updated = update_tasks(task_list,identifier,title if title else None,description if description else None,priority if priority else None,condition if condition else None)

                print ("updated data" if updated else "There is no data to update.")




            elif option == "5":
                identifier = input("enter the identifier of the task you want to delete ")
                delete = delete_task(task_list,identifier)
                print("delete" if delete else "No task was found with that identifier")


            elif option == "6":
                sw = False
                break

            else:
                print("invalid option")
                break    
    



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        except ValueError:
            print("error")














main()        




































































