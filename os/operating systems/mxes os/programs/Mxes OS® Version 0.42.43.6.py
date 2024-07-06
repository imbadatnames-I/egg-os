import os
import hashlib
import time
import pytz
from datetime import datetime
import random
from typing import List
current_entry = []
keywords=["task manager","shutdown","text doc","password manager","clock","journal","math","standby","text style","help","guess the number","settings"]
def get_user_info():
    if os.path.exists("user_info.txt"):
        with open("c:\\operating systems\\mxes os\\user_info.txt", "r") as file:
            lines = file.readlines()
            return lines
    return None

def save_user_info(username, password, hint, max_guesses, permission_level):
    with open("c:\\operating systems\\mxes os\\user_info.txt", "w") as file:
        file.write(f"{username}\n{password}\n{hint}\n{max_guesses}\n{permission_level}")

def authenticate(username, password, hint, max_guesses):
    attempts = 0
    locked_time = 15
    while attempts < int(max_guesses):
        print(f"\033[1;32;48mHello {username}, please enter your password:")
        guess = input()
        guess_settings=guess
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
    username, password, hint, max_guesses,permission_level = user_info
    if authenticate(username.strip(), password.strip(), hint.strip(), max_guesses.strip()):
        # Continue with authenticated user
        pass
    else:
        print("Authentication failed.")
else:
    print("Welcome to the Mxes OS (R)!")
    username = input("What do you want to name your account? ")
    password = hashlib.sha256(input("Please enter your password: ").encode()).hexdigest()
    hint = input("What is the password hint? ")
    max_guesses = input("How many wrong guesses until guesses are frozen for a duration? ")
    admin_code=input("if you have admin code input it here")
    if admin_code==98086:
        permission_level="admin"
    else:
        permission_level="user"
    save_user_info(username, password, hint, max_guesses,permission_level)
    print("Account created successfully!")
print("                                               _ __ ___ __  _____  ___     ___  ___ ")
print("                                              | '_ ` _ /\ \/ / _ \/ __|   / _ \/ __|")
print("                                              | | | | | |>  <  __/\__ \  | (_) \__ \ ")
print("                                              |_| |_| |_/_/\_\___||___/   \___/|___/")
print("")
print("")
print("")
print("                                             Stir Stick(R) Mxes OS (R) Version 0.98")
print("                                              (C)Copyright Stir Stick Corp 2024-2024")
print("                                                      press enter to start")
print("")
print("")
print("")
e=input()
running=True
z=0
clock_lock=False
end=False
program="standby"
print ("input help for a list of all programs. ")
while running==True:
    if program=="standby":
        program=input("what program do you want to run? ")
    if program=="task manager":
        def get_current_time_cst():
            current_time_utc = time.gmtime()  # Get current time in UTC
            current_time_cst = time.localtime(time.mktime(current_time_utc) - 5 * 3600)  # Subtract 5 hours for CST
            return time.strftime("%Y-%m-%d %H:%M:%S", current_time_cst)

        def add_task():
            task_name = input("What is the name of the task? ")
            task_state = input("Is the task finished or not? ")
            task_dis = input("What is the description? If there is none, type 'null' ")
            time_added = get_current_time_cst()
            with open("c:\\operating systems\\mxes os\\tasks.txt", "a") as file:
        # Check if the file is empty
                file.seek(0, 2)  # Move to the end of the file
                if file.tell() != 0:  # If file is not empty
                    file.write("\n")  # Add newline if not the first task
                file.write(f"Task: {task_name}, State: {task_state}\nDescription: {task_dis}\nTime Added: {time_added}\n")
        def edit_task():
            task_loc = int(input("What is the line of the name? "))
            new_name = input("What is the new name of the task? ")
            task_state = input("Is the task finished or not? ")
            task_dis = input("What is the description? If there is none, type 'null' ") 
            time_added = get_current_time_cst()
            with open("c:\\operating systems\\mxes os\\tasks.txt", "r") as file:
                lines = file.readlines(task_loc)
            with open("c:\\operating systems\\mxes os\\tasks.txt", "w") as file:
                file.write(f"Task: {new_name}, State: {task_state}\nDescription: {task_dis}\nTime Added: {time_added}\n")
                print("Name changed")
        def delete_task():
            del_task = input("What is the name of the task you want to delete? ")
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
                    print("Task deleted successfully.")
                else:
                    print("Task not found.")
        def view_tasks():
            with open("c:\\operating systems\\mxes os\\tasks.txt", "r") as file:
                tasks = file.readlines()
                for task in tasks:
                    print(task.strip())  # Strip to remove newline character
        while end==False:
            operation = input("Do you want to add, edit, delete, view tasks, or end program? ")
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
    elif program=="shutdown":
        while end==False:
            shutdown_confirmation=input("Mxes OS (R) is shutting down are you sure? t/f ")
            if shutdown_confirmation=="t":
                running=False
                print ("shutting down Mxes OS (R)")
                break
            elif shutdown_confirmation=="f":
                print("shutdown stopped")
                running=True
                program="standby"
            else:
                print("Invalid input")
            end=True
    elif program == "text doc":
        if end==False:
            txt_name = input("What is the name of your document? ")
            print("")
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
            if txt_op == "write":
                with open(txt_name, "a") as file:
                    # Check if the last line is empty
                    file.seek(0, 2)  # Move to the end of the file
                    file.write("\n")
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
    elif program=="password":
        # Function to read all passwords from file
        def read_passwords():
            with open("c:\\operating systems\\mxes os\\password_list.txt", "r") as file:
                return file.readlines()
        
        # Function to write all passwords to file
        def write_passwords(lines):
            with open("c:\\operating systems\\mxes os\\password_list.txt", "w") as file:
                file.writelines(lines)
    
        # Function to add a new password
        def add_password():
            password_site = input("Name of the site? ")
            account_name = input("Account name? ")
            password = input("Password? ")
    
            with open("c:\\operating systems\\mxes os\\password_list.txt", "a") as file:
                if file.tell() > 0:
                    file.write("\n")  # Ensure newline between entries
                file.write(f"{password_site}: {account_name} / {password}")
    
        # Function to edit an existing password
        def edit_password():
            lines = read_passwords()
            site_line_number = int(input("Line number of the site to edit? "))
        
            if 0 <= site_line_number < len(lines):
                new_site = input("New site name: ")
                new_account = input("New account name: ")
                new_password = input("New password: ")
    
                # Reconstruct the line with updated data
                lines[site_line_number] = f"{new_site}: {new_account} / {new_password}"
                write_passwords(lines)
                print("Password entry edited.")
            else:
                print("Invalid line number.")
    
        # Function to delete a password entry
        def delete_password():
            lines = read_passwords()
            line_number = int(input("Line number of the site to delete? "))
        
            if 0 <= line_number < len(lines):
                lines.pop(line_number-1)  # Remove the line
                lines.pop(line_number)
                lines.pop(line_number+1)
                write_passwords(lines)
                print("Password entry deleted.")
            else:
                print("Invalid line number.")
    
        # Function to view all passwords
        def view_passwords():
            lines = read_passwords()
            for idx, line in enumerate(lines):
                print(f"{idx}: {line.strip()}")
        while not end:
            operation = input("Do you want to add, edit, delete, view passwords, or end program? ")
            if operation == "end":
                end = True
                program="standby"
            elif operation == "add":
                add_password()
            elif operation == "edit":
                edit_password()
            elif operation == "delete":
                delete_password()
            elif operation == "view passwords":
                view_passwords()
            else:
                print("Invalid operation. Please try again.")
    elif program=="calendar":
        while end==False:
            calen_input=input("this is a place holder and isn't done")
            if calen_input=="end":
                end=True
    elif program=="text style":
        # Ask user for style, foreground, and background codes
        background_color = input("Enter background color code (e.g., 40 for gray, 41 for red, 42 for green, 43 for yellow, 44 for blue, 45 for magenta, 46 for cyan \nand 47 for white): ")
        foreground_color = input("Enter text color code (e.g., 30 for gray, 31 for red, 32 for green, 33 for yellow, 34 for blue, 35 for magenta, 36 for cyan \nand 37 for white): ")
        style = input("Enter text style code (0 for normal, 1 for bold, 4 for underline): ")
        
        # Construct the ANSI escape sequence
        ansi_escape = f"\033[{style};{foreground_color};{background_color}m"
        
        # Print the text with the chosen colors and style, followed by a reset
        print(f"{ansi_escape}This is styled text.")  # Reset at the end to avoid affecting further output
        end=True
    elif program=="clock":
        while not end:
            import time
            current_time_utc = time.gmtime()  # Get current time in UTC
            current_time_cst = time.localtime(time.mktime(current_time_utc) - 5 * 3600)  # Convert to CST
            formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time_cst)  # Format time
            print("the time is",formatted_time)  # Print the time
            end=True
    elif program=="guess the number":
        while not end:
            print ('how meny guesses do you want')
            guesses=int(input())+1
            guesses=guesses-1
            print('how big is the range use 1 number')
            y=int(input())
            number=random.randint(1,y)
            while guesses>0:
                print ('what is your geuss?')
                geuss_game=int(input())
                geuss=geuss_game
                if geuss==92675:
                    end=True
                    program="standby"
                    break
                if geuss_game==number:
                    if geuss!=92675:
                        print ('you got it right and the number is',number)
                        print ('it took',z+1,'attempts for you to find the number',number,"you had",guesses,"guesses left")
                        guesses=int(input("how meny guesses do you want? "))+1
                        y=int(input("how big is the range use 1 number"))
                        number=random.randint(1,y)
                        end=True
                        program="standby"
                else:
                    x=number-geuss
                    if x<1:
                        print ('number is to big')
                    else:
                        print('number is to small')
                guesses=guesses-1
                z=z+1
                
            if geuss==number:
                print ('you got it right and the number is',number)
                print ('it took',z+1,'attempts for you to find the number',number,"you had",guesses,"guesses left")
            else:
                x=number-geuss_game
                if x<1:
                    x=x*-2/2
                if x==1:
                    print("wrong your last geuss was",x,"number off",number)
                else:
                    print("wrong your last geuss was",x,"numbers off",number) 
    elif program=="math":
        while not end:
            import re
            def calculate(expression):
                valid_characters = re.match(r'^[d0-9+\-*/n().e\s]+$', expression)
                if not valid_characters:
                    return "Error: Invalid characters in expression."
                try:
                    result = eval(expression)
                    return result
                except Exception as e:
                    return f"Error: {e}"
            expression = input("Enter a mathematical expression: ")
            if expression=="end":
                end=True
            result = calculate(expression)
            print("Result:", result)
    elif program=="journal":
        print("Input journal entry. Type '$next$' to create a new entry, '$end$' to exit, or '$view$' to see previous entries.")
        journal_filename = f"{username}'s journal"
        while not end:
            journal_input = input("> ")
        
            # Get current CST time in ISO 8601 format
            cst_tz = pytz.timezone("US/Central")
            current_time = datetime.now(cst_tz).strftime("%Y-%m-%d %H:%M:%S")
        
            if journal_input == "$end$":
                end = True
            elif journal_input == "$view$":
                # Read and display all journal entries
                try:
                    with open(journal_filename, "r") as file:
                        full_journal = file.read()
                    print("\n--- Journal Entries ---\n")
                    print(full_journal)
                except FileNotFoundError:
                    print("No journal entries found.")
        
            elif journal_input == "$next$":
                # Save the current entry and start a new one
                if current_entry:
                    with open(journal_filename, "a") as file:
                        file.write(f"{current_time}:\n" + "\n".join(current_entry) + "\n\n")
        
            else:
                # Append the user input to the current entry list
                current_entry.append(journal_input)
    elif program=="help":
        if end==False:
            print("")
            print("task manager is a program that lets you add, delete, edit, and view all saved tasks")
            print("shutdown is a program that shutsdown the program after you confirm that you want to shut down the program with a t or f question")
            print("calendar is a program that is not done so don't use it yet") #remove after adding calendar
            print("standby is a program that is running after you boot up the program and after you leave every one exept shutdown.")
            print("text doc is a program that lets you write a file view the file and edit the file by inputing the command in [] and to leve edit mode input 0 when it asks for the line")
            print("text style is a program that changes the color of text or of the backround")
            print("password is a program that lets you save edit delete and view tasks with site username and password info.")
            print("journal is a program that lets you make journal enterys save them and view them later")
            print("clock is a program that tells you the time before ending. ")
            print("guess the number is a program where you try to guess a random number that is made with the range you give and you pick how meny guesses you get.")
            print("settings is a program that lets you change your password and view the rest of your data and the credits")
            print("")
            end=True
    elif program=="settings":
        while not end:
            settings_options = """
            1. View account settings
            2. Reset password
            3. Exit
            4. credits
            """
            print(settings_options)
            
            option = input("Choose an option: ")
            get_user_info()
            if option == "1":
                print("")
                print(f"Username: {username}")
                print(f"hint: {hint}")
                print(f"max guesses: {max_guesses}")
                print(f"Permission Level: {permission_level}")
        
            elif option == "2":
                # Reset password
                new_password = input("Enter new password: ")
                # Update user info (hashed password)
                save_user_info(username,hashlib.sha256(new_password.encode()).hexdigest(),hint,max_guesses,permission_level)
                print("Password has been updated.")
        
            elif option == "3":
                # Exit
                end=True
            
            elif option=="4":
                print("created by: connor orlow\ntested by: arianna orlow\nideas by: connor orlow and chatgpt\ninput enter to continue")
                input()
            else:
                print("Invalid option. Try again.")
    if end==True:
        end=False
        program="standby"
    if program not in keywords:
        print(program," is not a valid program")
        program="standby"