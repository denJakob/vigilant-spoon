new_task_content = Element("new-task-content")

def add_task_event(e):
    if e.key == "Enter":
        print(new_task_content.element.value)






new_task_content.element.onkeypress = add_task_event
