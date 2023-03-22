new_task_content = Element("new-task-content")


def test():
    print(new_task_content.element.value)

def add_task_event(e):
    if e.key == "Enter":
        test()






new_task_content.element.onkeypress = add_task_event
