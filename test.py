new_task_content = Element("new-task-content")

def add_task_event(e):
    if e.key == "Enter":
        print(e)






new_task_content.element.onkeypress = add_task_event
