def add_task(identifier:int,title:str,description:str,priority:str,condition:str,task_list):
    new_task = {
        "identifier":identifier,
        "title":title,
        "description":description,
        "priority":priority,
        "condition":condition
    }

    task_list.append(new_task)


def show_tasks(task_list):
    if not task_list:
        print("There are no assigned tasks")

    for new_task in task_list:
        print(f"identifier: {new_task["identifier"]}, title:{new_task["title"]}, description: {new_task["description"]}, priority: {new_task["priority"]}, condition: {new_task["condition"]} ")



def search_tasks(task_list,identifier):
    for new_task in task_list:

        if str(new_task["identifier"]) == str(identifier):
            return new_task
        
    return "task not found"



def update_tasks(task_list,identifier,new_title=None,new_description=None,new_priority=None,new_condition=None):
    result = search_tasks(task_list,identifier)

    if result is None or result == "task not found":
        return False
    
    if new_title is not None:
        result ["title"] = new_title

    if new_description is not None:
        result ["description"] = new_description

    if new_priority is not None:
        result ["priority"] = new_priority

    if new_condition is not None:
        result ["condition"] = new_condition

    return True


def delete_task(task_list,identifier):
    new_task = search_tasks(task_list,identifier)
    if new_task:
        task_list.remove(new_task)
        return True
    return False
                                      





                                      

    