import os
import hashlib
import time

def get_user_info():
    if os.path.exists("user_info.txt"):
        with open("c:\\os\\operating systems\\mxes os\\user_info.txt", "r") as file:
            lines = file.readlines()
            return lines
    return None

def save_user_info(username, password, hint, max_guesses):
    with open(username+"info", "w") as file:
        file.write(f"{username}\n{password}\n{hint}\n{max_guesses}")
start_op=input("do you want to startup, change account, edit account, make a new account, or delete account")
if start_op=="new account":
    username = input("What do you want to name your account? ")
    password = hashlib.sha256(input("Please enter your password: ").encode()).hexdigest()
    hint = input("What is the password hint? ")
    max_guesses = input("How many wrong guesses until guesses are frozen for a duration? ")
    save_user_info(username, password, hint, max_guesses)
    print("Account created successfully!")
    with open("c:\\os\\operating systems\\mxes os\\accounts info","w") as file:
        file.seek(0,2)
        file.write(username)
        file.write("\n")
if start_op=="change account":
    with open("c:\\os\\operating systems\\mxes os\\accounts list",'r') as file:
        accounts=file.readlines()
elif start_op=="startup":
    def authenticate(username, password, hint, max_guesses):
        attempts = 0
        locked_time = 15
        while attempts < int(max_guesses):
            print(f"Hello {username}, please enter your password:")
            guess = input()
            if hashlib.sha256(guess.encode()).hexdigest() == password:
                print("Authentication successful!")
                return True
            else:
                attempts += 1
                print("Incorrect password.")
                if attempts == 1:
                    print("Hint:", hint)
                if attempts == int(max_guesses):
                    print(f"Too many incorrect attempts. Guesses locked for {locked_time} seconds.")
                    time.sleep(locked_time)
                    attempts = 0
                    locked_time *= 2
        return False

    user_info = get_user_info()
    if user_info:
        username, password, hint, max_guesses = user_info
        if authenticate(username.strip(), password.strip(), hint.strip(), max_guesses.strip()):
            pass
        else:
            print("Authentication failed.")
    else:
        print("Welcome to the Mxes OS (R)!")
        username = input("What do you want to name your account? ")
        password = hashlib.sha256(input("Please enter your password: ").encode()).hexdigest()
        hint = input("What is the password hint? ")
        max_guesses = input("How many wrong guesses until guesses are frozen for a duration? ")
        save_user_info(username, password, hint, max_guesses)
        print("Account created successfully!")
        with open("c:\\os\\operating systems\\mxes os\\accounts info","w") as file:
            file.write(username)
print("                                               _ __ ___ __  _____  ___     ___  ___ ")
print("                                              | '_ ` _ /\ \/ / _ \/ __|   / _ \/ __|")
print("                                              | | | | | |>  <  __/\__ \  | (_) \__ \ ")
print("                                              |_| |_| |_/_/\_\___||___/   \___/|___/")
print('')
print('')
print('')
print('                                             Stir Stick(R) Mxes OS (R) Version 0.90')
print('                                              (C)Copyright Stir Stick Corp 2024-2024')
print('                                                      press enter to start')
print('')
print('')
print('')
e=input()
running=True
end=False
program="standby"
print ('type i for a list of all programs and short description of them. ')
while running==True:
    if program=="standby":
        program=input("what program do you want to run? ")
    if program=="task manager":
        def get_current_time_cst():
            current_time_utc = time.gmtime()  # Get current time in UTC
            current_time_cst = time.localtime(time.mktime(current_time_utc) - 5 * 3600)  # Subtract 5 hours for CST
            return time.strftime("%Y-%m-%d %H:%M:%S", current_time_cst)

        def add_task():
            task_name = input('What is the name of the task? ')
            task_state = input('Is the task finished or not? ')
            task_dis = input('What is the description? If there is none, type "null" ')
            time_added = get_current_time_cst()
            with open("c:\\os\\operating systems\\mxes os\\tasks.txt", "a") as file:
        # Check if the file is empty
                file.seek(0, 2)  # Move to the end of the file
                if file.tell() != 0:  # If file is not empty
                    file.write("\n")  # Add newline if not the first task
                file.write(f"Task: {task_name}, State: {task_state}\nDescription: {task_dis}\nTime Added: {time_added}\n")
        def edit_task():
            task_loc = int(input('What is the line of the name? '))
            new_name = input('What is the new name of the task? ')
            task_state = input('Is the task finished or not? ')
            task_dis = input('What is the description? If there is none, type "null" ') 
            time_added = get_current_time_cst()
            with open("c:\\os\\operating systems\\mxes os\\tasks.txt", "r") as file:
                lines = file.readlines(task_loc)
            with open("c:\\os\\operating systems\\mxes os\\tasks.txt", "w") as file:
                file.write(f"Task: {new_name}, State: {task_state}\nDescription: {task_dis}\nTime Added: {time_added}\n")
                print("Name changed")
        def delete_task():
            del_task = input('What is the name of the task you want to delete? ')
            with open("c:\\os\\operating systems\\mxes os\\tasks.txt", "r") as file:
                lines = file.readlines()  # Read all lines from the file
            with open("c:\\os\\operating systems\\mxes os\\tasks.txt", "w") as file:
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
                    print("Task deleted successfully.")
                else:
                    print("Task not found.")
        def view_tasks():
            with open("c:\\os\\operating systems\\mxes os\\tasks.txt", "r") as file:
                tasks = file.readlines()
                for task in tasks:
                    print(task.strip())  # Strip to remove newline character
        while end==False:
            operation = input('Do you want to add, edit, delete, view tasks, or end program? ')
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
                print("Invalid operation. Please try again.")
    if program=="shutdown":
        while end==False:
            shutdown_confirmation=input("Mxes OS (R) is shutting down are you sure? t/f ")
            if shutdown_confirmation=="t":
                running=False
                print ('shutting down Mxes OS (R)')
                break
            elif shutdown_confirmation=="f":
                print("shutdown stopped")
                running=True
                end=True
            else:
                print('Invalid input')
    elif program == "text doc":
        if end==False:
            txt_name = input("What is the name of your document? ")
            print('')
            txt_op="write"
        while not end:
            if txt_op=="write":
                txt_in = input()
            if txt_in=="[edit]":
                txt_op="edit"
            if txt_in=="[write]":
                txt_op=="write"
            if txt_in=="[view]":
                txt_op="view"
            if txt_in=="[end]":
                txt_op="end"
            if txt_op == 'write':
                with open(txt_name, "a") as file:
                    # Check if the last line is empty
                    file.seek(0, 2)  # Move to the end of the file
                    file.write('\n')
                    file.write(txt_in)  # Write user input to the file
            if txt_op == "end":
                end = True
                program=="standby"
                print(end,program)
            elif txt_op == "edit":
                old_line = int(input("What line is being edited? ")) - 1  # Adjust to 0-indexed line number
                with open(txt_name, "r") as file:
                    lines = file.readlines()
                if old_line==-1:
                    end=True
                if old_line < -1 or old_line >= len(lines):
                    print("Invalid line number.")
                elif old_line>0:
                    old_content = lines[old_line].strip()  # Get the content of the old line
                    new_content = input(f"Current content: {old_content}\nNew content: ")  # Prompt for new content
                    lines[old_line] = new_content  # Update the line with the new content
        with open(txt_name, "w") as file:
            file.writelines(lines)
            if txt_op == "view":
                with open(txt_name, "r") as file:
                    lines = file.readlines()
                    for line in lines:
                        print(line.strip())
                    txt_op = "write"  # Exit the loop after printing the tex
    elif program=="calendar":
        while end==False:
            calen_input=input("this is a place holder and isn't done")
            if calen_input=="end":
                end=True
    elif program=="i":
        if end==False:
            print('')
            print('task manager is a program that lets you add, delete, edit, and view all saved tasks')
            print('shutdown is a program that shutsdown the program after you confirm that you want to shut down the program with a t or f question')
            print("calendar is a program that is not done so don't use it yet") #remove after adding calendar
            print('standby is a program that is running after you boot up the program and after you leave every one exept shutdown.')
            print('text doc is a program that lets you write a file view the file and edit the file by inputing the command in [] and to leve edit mode input 0 when it asks for the line')
            print('')
            end=True
    if end==True:
        end=False
        program="standby"
    if program !="standby" or "shutdown":
        print (program,'is a invalid program')
        program="standby"
