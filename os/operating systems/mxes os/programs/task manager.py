import time
import os
import pyttsx3 # type: ignore
engine = pyttsx3.init()
end=False
def get_user_info():
                    if os.path.exists("user_info.txt"):
                        with open("c:\\operating systems\\mxes os\\user_info.txt", "r") as file:
                            lines = file.readlines()
                            return lines
                    return None
user_info = get_user_info()
username, password, hint, max_guesses,permission_level,tts_mode = user_info
def get_current_time_cst():
    current_time_utc = time.gmtime()  # Get current time in UTC
    current_time_cst = time.localtime(time.mktime(current_time_utc) - (6 * 3600))  # Subtract 5 hours for CST
    return time.strftime("%Y-%m-%d %H:%M:%S", current_time_cst)
def add_task():
    if tts_mode=="t":
        engine.say("What is the name of the task?")
        engine.runAndWait()
    task_name = input("> What is the name of the task? \n> ")
    if tts_mode=="t":
        engine.say("Is the task finished or not?")
        engine.runAndWait()
    task_state = input("> Is the task finished or not? \n> ")
    if tts_mode=="t":
        engine.say("What is the description? If there is none, type 'null'")
        engine.runAndWait()
    task_dis = input("> What is the description? If there is none, type 'null' \n> ")
    time_added = get_current_time_cst()
    with open("c:\\operating systems\\mxes os\\tasks.txt", "a") as file:
# Check if the file is empty
        file.seek(0, 2)  # Move to the end of the file
        if file.tell() != 0:  # If file is not empty
            file.write("\n")  # Add newline if not the first task
        file.write(f"Task: {task_name}, State: {task_state}\nDescription: {task_dis}\nTime Added: {time_added}\n")
def edit_task():
    if tts_mode=="t":
            engine.say(f"What is the line of the name?")
            engine.runAndWait()
    task_loc = int(input("> What is the line of the name? \n> "))
    if tts_mode=="t":
            engine.say(f"What is the new name of the task?")
            engine.runAndWait()
    new_name = input("> What is the new name of the task? \n> ")
    if tts_mode=="t":
            engine.say(f"Is the task finished or not?")
            engine.runAndWait()
    task_state = input("> Is the task finished or not? \n> ")
    if tts_mode=="t":
            engine.say(f"What is the description? If there is none, type 'null'")
            engine.runAndWait()
    task_dis = input("> What is the description? If there is none, type 'null' \n> ")
    time_added = get_current_time_cst()
    with open("c:\\operating systems\\mxes os\\tasks.txt", "r") as file:
        lines = file.readlines(task_loc)
    with open("c:\\operating systems\\mxes os\\tasks.txt", "w") as file:
        file.write(f"Task: {new_name}, State: {task_state}\nDescription: {task_dis}\nTime Added: {time_added}\n")
        print("> Name changed")
        if tts_mode=="t":
            engine.say(f"name changed")
            engine.runAndWait()
def delete_task():
    if tts_mode=="t":
            engine.say(f"What is the name of the task you want to delete?")
            engine.runAndWait()
    del_task = input("> What is the name of the task you want to delete? \n> ")
    with open("c:\\operating systems\\mxes os\\tasks.txt", "r") as file:
        lines = file.readlines()  # Read all lines from the file
    with open("c:\\operating systems\\mxes os\\tasks.txt", "w") as file:
        task_deleted = False
        i = 0
        while i < len(lines):
            if f"Task: {del_task}" in lines[i]:
                task_deleted = True
                # Skip current line (task name and state) and the next two lines
                i += 4
            else:
                file.write(lines[i])
                i += 1
                if task_deleted:
                    print("> Task deleted successfully.")
                    if tts_mode=="t":
                        engine.say(f"Task deleted successfully.")
                        engine.runAndWait()
                else:
                    print("> Task not found.")
                if tts_mode=="t":
                    engine.say(f"Task not found")
                    engine.runAndWait()
def view_tasks():
    with open("c:\\operating systems\\mxes os\\tasks.txt", "r") as file:
        tasks = file.readlines()
        for task in tasks:
            print(task.strip())  # Strip to remove newline character
            if tts_mode=="t":
                engine.say(task.strip())
                engine.runAndWait()
while not end:
    if tts_mode=="t":
        engine.say("Do you want to add, edit, delete, view tasks, or end program?")
        engine.runAndWait()
    operation = input("> Do you want to add, edit, delete, view tasks, or end program? \n> ")
    if operation == "end":
        end=True
    elif operation == "add":
        add_task()
    elif operation == "edit":
        edit_task()
    elif operation == "delete":
        delete_task()
    elif operation == "view tasks":
        view_tasks()
    else:
        print("> Invalid operation. Please try again.")
        if tts_mode=="t":
            engine.say(f"Invalid operation. Please try again.")
            engine.runAndWait()