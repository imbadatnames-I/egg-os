import os
import hashlib
import time
from datetime import datetime
import random
from typing import List
import winsound
import pyttsx3 # type: ignore
winsound.PlaySound("mxes os startup.wav", winsound.SND_ASYNC)
current_entry = []
ansi_escape = "\033[1;32;48m"
keywords=["task manager","shutdown","text doc","password manager","clock","journal","math","standby","text style","help","guess the number","settings","recipe","dice","wordle","money","version finder"]
def get_user_info():
    if os.path.exists("user_info.txt"):
        with open("c:\\os\\operating systems\\mxes os\\user_info.txt", "r") as file:
            lines = file.readlines()
            return lines
    return None
def save_user_info(username, password, hint, max_guesses, permission_level, tts_mode):
    with open("c:\\os\\operating systems\\mxes os\\user_info.txt", "w") as file:
        file.write(f"{username}\n{password}\n{hint}\n{max_guesses}\n{permission_level}\n{tts_mode}")
def authenticate(username, password, hint, max_guesses):
    attempts = 0
    locked_time = 15
    while attempts < int(max_guesses):
        if tts_mode=="t":
                time.sleep(2)
                engine = pyttsx3.init()
                engine.say(f"Hello {username} please enter your password:")
                engine.runAndWait()
        guess=input(f"{ansi_escape}> Hello {username} please enter your password:\n> ")
        guess_settings=guess
        if hashlib.sha256(guess.encode()).hexdigest() == password:
            print("> Authentication successful!")
            if tts_mode=="t":
                engine = pyttsx3.init()
                engine.say("Authentication successful!")
                engine.runAndWait()
            return True
        else:
            attempts += 1
            print("> Incorrect password.")
            if tts_mode=="t":
                engine = pyttsx3.init()
                engine.say("Incorrect password")
                engine.runAndWait()
            if attempts == 1:
                print("> Hint:", hint)
                if tts_mode=="t":
                    engine = pyttsx3.init()
                    engine.say(f"hint: {hint}")
                    engine.runAndWait()
            if attempts == int(max_guesses):
                print(f"> Too many incorrect attempts. Guesses locked for {locked_time} seconds.")
                if tts_mode=="t":
                    engine.say(f"Too many incorrect attempts. Guesses locked for {locked_time} seconds.")
                    engine.runAndWait()
                time.sleep(locked_time)
                attempts = 0
                locked_time *= 2
    return False
user_info = get_user_info()
if user_info:
    username, password, hint, max_guesses,permission_level,tts_mode = user_info
    if authenticate(username.strip(), password.strip(), hint.strip(), max_guesses.strip()):
        # Continue with authenticated user
        pass
    else:
        print("> Authentication failed.")
        if tts_mode=="t":
            engine = pyttsx3.init()
            engine.say(f"Authentication failed")
            engine.runAndWait()
        exit()
else:
    print("\033[1;32;48m> Welcome to the Mxes OS ®!")
    username = input("> What do you want to name your account? ")
    password = hashlib.sha256(input("> Please enter your password: ").encode()).hexdigest()
    hint = input("> What is the password hint? ")
    max_guesses = input("> How many wrong guesses until guesses are frozen for a duration? ")
    tts_mode=input("> Do you want tts?")
    admin_code=input("> if you have admin code input it here")
    if admin_code==98086:
        permission_level="> admin"
    else:
        permission_level="> user"
    save_user_info(username, password, hint, max_guesses,permission_level,tts_mode)
    print("> Account created successfully!")
print(">                                               _ __ ___ __  _____  ___     ___  ___ ")
print(">                                              | '_ ` _ /\ \/ / _ \/ __|   / _ \/ __|")
print(">                                              | | | | | |>  <  __/\__ \  | (_) \__ \ ")
print(">                                              |_| |_| |_/_/\_\___||___/   \___/|___/")
print("> ")
print("> ")
print("> ")
print(">                                            Stir Stick® Mxes OS® Version 0.97.15.6")
print(f">                                                  ©Stir Stick Corp 2024-{datetime.now().year}")
print(">                                                     press enter to start")
print("> ")
print("> ")
print("> ")
if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("press enter to start")
                            engine.runAndWait()
e=input("> ")
running=True
z=0
clock_lock=False
end=False
program="standby"
print ("> input help for a list of all programs.")
if tts_mode=="t":
    engine = pyttsx3.init()
    engine.say("input help for a list of all programs.")
    engine.runAndWait()
while running==True:
    if program=="standby":
        if tts_mode=="t":
            engine = pyttsx3.init()
            engine.say("what program do you want to run?")
            engine.runAndWait()
        program=input("> what program do you want to run? \n> ")
    elif program=="task manager":
        def get_current_time_cst():
            current_time_utc = time.gmtime()  # Get current time in UTC
            current_time_cst = time.localtime(time.mktime(current_time_utc) - 5 * 3600)  # Subtract 5 hours for CST
            return time.strftime("%Y-%m-%d %H:%M:%S", current_time_cst)
        def add_task():
            if tts_mode=="t":
                engine = pyttsx3.init()
                engine.say("What is the name of the task?")
                engine.runAndWait()
            task_name = input("> What is the name of the task? \n> ")
            if tts_mode=="t":
                engine = pyttsx3.init()
                engine.say("Is the task finished or not?")
                engine.runAndWait()
            task_state = input("> Is the task finished or not? \n> ")
            if tts_mode=="t":
                engine = pyttsx3.init()
                engine.say("What is the description? If there is none, type 'null'")
                engine.runAndWait()
            task_dis = input("> What is the description? If there is none, type 'null' \n> ")
            time_added = get_current_time_cst()
            with open("c:\\os\\operating systems\\mxes os\\tasks.txt", "a") as file:
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
            with open("c:\\os\\operating systems\\mxes os\\tasks.txt", "r") as file:
                lines = file.readlines(task_loc)
            with open("c:\\os\\operating systems\\mxes os\\tasks.txt", "w") as file:
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
            with open("c:\\os\\operating systems\\mxes os\\tasks.txt", "r") as file:
                tasks = file.readlines()
                for task in tasks:
                    print(task.strip())  # Strip to remove newline character
                    if tts_mode=="t":
                        engine.say(task.strip())
                        engine.runAndWait()
        while not end:
            if tts_mode=="t":
                engine = pyttsx3.init()
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
    elif program=="shutdown": 
        while end==False:
            if tts_mode=="t":
                        engine.say(f"Mxes OS ® is shutting down are you sure? t/f")
                        engine.runAndWait()
            shutdown_confirmation=input("> Mxes OS ® is shutting down are you sure? t/f \n> ")
            if shutdown_confirmation=="t":
                running=False
                print ("> shutting down Mxes OS ®")
                if tts_mode=="t":
                        engine.say(f"shutting down Mxes OS ®")
                        engine.runAndWait()
                break
            elif shutdown_confirmation=="f":
                print("> shutdown stopped")
                if tts_mode=="t":
                        engine.say(f"shutdown stopped")
                        engine.runAndWait()
                running=True
                program="standby"
            else:
                print("> Invalid input")
                if tts_mode=="t":
                        engine.say(f"Invalid input")
                        engine.runAndWait()
            end=True
    elif program=="text doc":
        if end==False:
            txt_name = input("> What is the name of your document? \n> ")
            if tts_mode=="t":
                        engine.say(f"What is the name of your document?")
                        engine.runAndWait()
            print("> ")
            txt_op="write"
        while not end:
            if txt_op=="write":
                txt_in = input("> ")
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
            elif txt_op == "edit":
                old_line = int(input("> What line is being edited? \n> ")) - 1  # Adjust to 0-indexed line number
                if tts_mode=="t":
                        engine.say(f"What line is being edited")
                        engine.runAndWait()
                with open(txt_name, "r") as file:
                    lines = file.readlines()
                if old_line==-1:
                    end=True
                if old_line < -1 or old_line >= len(lines):
                    print("> Invalid line number.")
                    if tts_mode=="t":
                        engine.say(f"Invalid line number")
                        engine.runAndWait()
                elif old_line>0:
                    old_content = lines[old_line].strip()  # Get the content of the old line
                    new_content = input(f"> Current content: {old_content}\nNew content: \n> ")  # Prompt for new content
                    if tts_mode=="t":
                        engine.say(f"current content: {old_content}\nNew content:")
                        engine.runAndWait()
                    lines[old_line] = new_content  # Update the line with the new content
        with open(txt_name, "r") as file:
            lines = file.readlines()
        with open(txt_name, "w") as file:
            file.writelines(lines)
            if txt_op == "view":
                    for line in lines:
                        print(line.strip())
                        if tts_mode=="t":
                            engine.say(f"line.strip()")
                            engine.runAndWait()
                    txt_op = "write"  # Exit the loop after printing the tex
    elif program=="password":
        def read_passwords():
            with open("c:\\os\\operating systems\\mxes os\\password_list.txt", "r") as file:
                return file.readlines()    
        # Function to write all passwords to file
        def write_passwords(lines):
            with open("c:\\os\\operating systems\\mxes os\\password_list.txt", "w") as file:
                file.writelines(lines)
    
        # Function to add a new password
        def add_password():
            password_site = input("> Name of the site? \n> ")
            if tts_mode=="t":
                        engine.say(f"")
                        engine.runAndWait()
            account_name = input("> Account name? \n> ")
            password = input("> Password? \n> ")
    
            with open("c:\\os\\operating systems\\mxes os\\password_list.txt", "a") as file:
                if file.tell() > 0:
                    file.write("\n")  # Ensure newline between entries
                file.write(f"> {password_site}: {account_name} / {password}")
    
        # Function to edit an existing password
        def edit_password():
            lines = read_passwords()
            site_line_number = int(input("> Line number of the site to edit? "))
        
            if 0 <= site_line_number < len(lines):
                if tts_mode=="t":
                        engine.say(f"New site name:")
                        engine.runAndWait()
                new_site = input("> New site name: \n> ")
                if tts_mode=="t":
                        engine.say(f"New account name:")
                        engine.runAndWait()
                new_account = input("> New account name: \n> ")
                if tts_mode=="t":
                        engine.say(f"New password:")
                        engine.runAndWait()
                new_password = input("> New password: \n> ")
    
                # Reconstruct the line with updated data
                lines[site_line_number] = f"{new_site}: {new_account} / {new_password}"
                write_passwords(lines)
                print("> Password entry edited.")
                if tts_mode=="t":
                        engine.say(f"Password entry edited.")
                        engine.runAndWait()
            else:
                print("> Invalid line number.")
                if tts_mode=="t":
                        engine.say(f"Invalid line number.")
                        engine.runAndWait()
    
        # Function to delete a password entry
        def delete_password():
            lines = read_passwords()
            line_number = int(input("> Line number of the site to delete? \n> "))
            if tts_mode=="t":
                        engine.say(f"Line number of the site to delete?")
                        engine.runAndWait()
        
            if 0 <= line_number < len(lines):
                lines.pop(line_number-1)  # Remove the line
                lines.pop(line_number)
                lines.pop(line_number+1)
                write_passwords(lines)
                print("> Password entry deleted.")
                if tts_mode=="t":
                        engine.say(f"")
                        engine.runAndWait()
            else:
                print("> Invalid line number.")
                if tts_mode=="t":
                    engine.say(f"Password entry deleted.")
                    engine.runAndWait()
        # Function to view all passwords
        def view_passwords():
            lines = read_passwords()
            for idx, line in enumerate(lines):
                print(f"> {idx}: {line.strip()}")
                if tts_mode=="t":
                    engine.say(f"{idx}: {line.strip()}")
                    engine.runAndWait()
        while not end:
            operation = input("> Do you want to add, edit, delete, view passwords, or end program? \n> ")
            if tts_mode=="t":
                    engine.say(f"Do you want to add, edit, delete, view passwords, or end program?")
                    engine.runAndWait()
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
                print("> Invalid operation. Please try again.")
                if tts_mode=="t":
                    engine.say(f"Invalid operation. Please try again.")
                    engine.runAndWait()
    elif program=="calendar":
        while end==False:
            calen_input=input("> this is a place holder and isn't done\n> ")
            if calen_input=="end":
                end=True
    elif program=="text style":
        # Ask user for style, foreground, and background codes
        if tts_mode=="t":
            engine.say(f"Enter background color code (e.g., 40 for gray, 41 for red, 42 for green, 43 for yellow, 44 for blue, 45 for magenta, 46 for cyan 47 for white and 48 for black):")
            engine.runAndWait()
        background_color = input("> Enter background color code (e.g., 40 for gray, 41 for red, 42 for green, 43 for yellow, 44 for blue, 45 for magenta, 46 for cyan \n> 47 for white and 48 for black): \n> ")
        if tts_mode=="t":
            engine.say(f"Enter text color code (e.g., 30 for gray, 31 for red, 32 for green, 33 for yellow, 34 for blue, 35 for magenta, 36 for cyan and 37 for white):")
            engine.runAndWait()
        foreground_color = input("> Enter text color code (e.g., 30 for gray, 31 for red, 32 for green, 33 for yellow, 34 for blue, 35 for magenta, 36 for cyan \nand 37 for white): \n> ")
        if tts_mode=="t":
            engine.say(f"Enter text style code (0 for normal, 1 for bold, 4 for underline):")
            engine.runAndWait()
        style = input("> Enter text style code (0 for normal, 1 for bold, 4 for underline): \n> ")
        
        # Construct the ANSI escape sequence
        ansi_escape = f"\033[{style};{foreground_color};{background_color}m"
        
        print(f"> {ansi_escape}This is styled text.")  # Reset at the end to avoid affecting further output
        end=True
    elif program=="clock":
        while not end:
            import time
            current_time_utc = time.gmtime()  # Get current time in UTC
            current_time_cst = time.localtime(time.mktime(current_time_utc) - 5 * 3600)  # Convert to CST
            formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time_cst)  # Format time
            print("> the time is",formatted_time)  # Print the time
            if tts_mode=="t":
                    engine.say(f"the time is",formatted_time)
                    engine.runAndWait()
            end=True
    elif program=="guess the number":
        while not end:
            print ("> how meny guesses do you want\n> ")
            if tts_mode=="t":
                engine = pyttsx3.init()
                engine.say("how meny guesses do you want")
                engine.runAndWait()
            guesses=int(input("> "))+1
            guesses=guesses-1
            print("> how big is the range use 1 number\n> ")
            if tts_mode=="t":
                engine = pyttsx3.init()
                engine.say("how big is the range use 1 number")
                engine.runAndWait()
            y=int(input("> "))
            number=random.randint(1,y)
            while guesses>0:
                if tts_mode=="t":
                    engine = pyttsx3.init()
                    engine.say("what is your geuss?")
                    engine.runAndWait()
                guess=input("> what is your geuss?\n> ")
                geuss_game=int(input("> "))
                if guess==92675:
                    end=True
                    program="standby"
                    break
                if geuss_game==number:
                    if guess!=92675:
                        if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say(f"you got it right and the number is,{number}")
                            engine.runAndWait()
                        print ('you got it right and the number is',number)
                        if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say('it took',z+1,'attempts for you to find the number',number,"you had",guesses,"guesses left")
                            engine.runAndWait()
                        print ('it took',z+1,'attempts for you to find the number',number,"you had",guesses,"guesses left")
                        if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("how meny guesses do you want?")
                            engine.runAndWait()
                        guesses=int(input("> how meny guesses do you want? \n> "))+1
                        if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("how big is the range use 1 number")
                            engine.runAndWait()
                        y=int(input("> how big is the range use 1 number\n> "))
                        number=random.randint(1,y)
                        end=True
                        program="standby"
                else:
                    x=number-guess
                    if x<1:
                        print ('> number is to big')
                        if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("number is to big")
                            engine.runAndWait()
                    else:
                        print('> number is to small')
                        if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("number is to small")
                            engine.runAndWait()
                guesses=guesses-1
                z=z+1
                
            if guess==number:
                print ('> you got it right and the number is',number)
                if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say('you got it right and the number is',number)
                            engine.runAndWait()
                print ('> it took',z+1,'attempts for you to find the number',number,"you had",guesses,"guesses left")
                if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say('it took',z+1,'attempts for you to find the number',number,"you had",guesses,"guesses left")
                            engine.runAndWait()
            else:
                x=number-geuss_game
                if x<1:
                    x=x*-2/2
                if x==1:
                    print("> wrong your last geuss was",x,"number off",number)
                    if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("wrong your last geuss was",x,"number off",number)
                            engine.runAndWait()
                else:
                    print("> wrong your last geuss was",x,"numbers off",number) 
                    if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("wrong your last geuss was",x,"numbers off",number)
                            engine.runAndWait()
    elif program=="math":
        while not end:
            import re
            def calculate(expression):
                valid_characters = re.match(r'^[d0-9+\-*/n().e\s]+$', expression)
                if not valid_characters:
                    if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("Error: Invalid characters in expression.")
                            engine.runAndWait()
                    return "Error: Invalid characters in expression."
                try:
                    result = eval(expression)
                    return result
                except Exception as e:
                    if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say(f"Error: {e}")
                            engine.runAndWait()
                    return f"Error: {e}"
            if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("Enter a mathematical expression:")
                            engine.runAndWait()
            expression = input("> Enter a mathematical expression: \n> ")
            if expression=="end":
                end=True
            result = calculate(expression)
            if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("Result:", result)
                            engine.runAndWait()
            print("> Result:", result)
    elif program=="journal":
        print("> Input journal entry. Type '$next$' to create a new entry, '$end$' to exit, or '$view$' to see previous entries\n> .")
        if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("Input journal entry. Type '$next$' to create a new entry, '$end$' to exit, or '$view$' to see previous entries")
                            engine.runAndWait()
        while not end:
            journal_input = input("> ")
        
            current_time_utc = time.gmtime()  # Get current time in UTC
            current_time_cst = time.localtime(time.mktime(current_time_utc) - 5 * 3600)  # Subtract 5 hours for CST
            current_time= time.strftime("%Y-%m-%d %H:%M:%S", current_time_cst)
        
            if journal_input == "$end$":
                end = True
            elif journal_input == "$view$":
                # Read and display all journal entries
                try:
                    with open("c:\\os\\operating systems\\mxes os\\journal", "r") as file:
                        full_journal = file.read()
                    print("> \n--- Journal Entries ---\n")
                    if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("Journal Entries")
                            engine.runAndWait()
                    print(full_journal)
                    if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("full_journal")
                            engine.runAndWait()
                except FileNotFoundError:
                    print("> No journal entries found.")
                    if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("No journal entries found")
                            engine.runAndWait()
            elif journal_input == "$next$":
                # Save the current entry and start a new one
                if current_entry:
                    with open("c:\\os\\operating systems\\mxes os\\journal", "a") as file:
                        file.write(f"> {current_time}:\n" + "\n".join(current_entry) + "\n\n")
        
            else:
                # Append the user input to the current entry list
                current_entry.append(journal_input)
    elif program=="help":
        if end==False:
            if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("Available Programs: task manager: Manage tasks (add, edit, delete, view). shutdown: Safely shut down the program after confirmation. text doc: Create, edit, and view text documents. password manager: Manage passwords (add, edit, delete, view). clock: Display the current time. journal: Record journal entries and view past entries. math: Perform mathematical calculations. standby: The initial state after starting the program. text style: Change the console text style and color. guess the number: A simple guessing game with a range and attempts. settings: Change account settings, including password. money: add or remove money or costs and view money report version finder: once you input the number of characters it will tell you the version number.")
                            engine.runAndWait()
            print("> ")
            print("> Available Programs:")
            print(">   task manager: Manage tasks (add, edit, delete, view).")
            print(">   shutdown: Safely shut down the program after confirmation.")
            print(">   text doc: Create, edit, and view text documents.")
            print(">   password manager: Manage passwords (add, edit, delete, view).")
            print(">   clock: Display the current time.")
            print(">   journal: Record journal entries and view past entries.")
            print(">   math: Perform mathematical calculations.")
            print(">   standby: The initial state after starting the program.")
            print(">   text style: Change the console text style and color.")
            print(">   guess the number: A simple guessing game with a range and attempts.")
            print(">   settings: Change account settings, including password.")
            print(">   money: add or remove money or costs and view money report")
            print(">   version finder: once you input the number of characters it will tell you the version number.")
            print("> ")
            end=True
    elif program=="settings":
        while not end:
            settings_options = """
>             1. View account settings
>             2. Reset password
>             3. Exit
>             4. Credits 
>"""
            print(">",settings_options)
            if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say(settings_options)
                            engine.runAndWait()
            if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("Choose an option:")
                            engine.runAndWait()
            option = input("> Choose an option: \n> ")
            get_user_info()
            if option == "1":
                print("> ")
                print(f"> Username: {username}\n> hint: {hint}\n> max guesses: {max_guesses}\n> Permission Level: {permission_level}")
                if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say(f"Username: {username} hint: {hint} max guesses: {max_guesses} Permission Level: {permission_level}")
                            engine.runAndWait()
            elif option == "2":
                # Reset password
                if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("Enter new password:")
                            engine.runAndWait()
                new_password = input("> Enter new password: \n> ")
                new_password=hashlib.sha256(new_password.encode()).hexdigest()
                with open("c:\\os\\operating systems\\mxes os\\user_info.txt", "w") as file:
                    file.write(f"{username}{new_password}\n{hint}{max_guesses}{permission_level}")
                    if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("Password has been updated")
                            engine.runAndWait()
                print("> Password has been updated.")
            elif option == "3":
                # Exit
                end=True
            elif option=="4":
                if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("created by: connor orlow tested by: arianna orlow ideas by: connor orlow and chatgpt name by: Arianna orlow input enter to continue")
                            engine.runAndWait()
                print("> created by: connor orlow\n> tested by: arianna orlow\n> ideas by: connor orlow and chatgpt\n> name by: Arianna orlow \n> input enter to continue")
                input("> ")
            else:
                print("> Invalid option. Try again.")
                if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("Invalid option. Try again.")
                            engine.runAndWait()
    elif program=="dice":
        while not end:
            if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("how many sides do these dice have? To leave type end.")
                            engine.runAndWait()
            dice_sides_number=input("> how many sides do these dice have? To leave type end. \n> ")
            if dice_sides_number.lower()=="end":
                end=True
            else:
                if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("How meny dice are there?")
                            engine.runAndWait()
                number_of_dice=input("> How meny dice are there?\n> ")
                dice_number_pr=1
                while number_of_dice>0:
                    dice_number=random.randint(1,dice_sides_number)
                    if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say(f"die {dice_number_pr} number is {dice_number}")
                            engine.runAndWait()
                    print(f"> die {dice_number_pr} number is {dice_number}")
                    dice_number_pr+=1
                    number_of_dice-=1
    elif program=="wordle":
        WORD_LENGTH = 5
        MAX_GUESSES = 5
        
        # Function to give feedback for a guess
        def get_feedback(guess, target_word):
            feedback = ["_"] * WORD_LENGTH
            used_indices = []
        
            # First, mark the correct positions
            for i in range(WORD_LENGTH):
                if guess[i] == target_word[i]:
                    feedback[i] = guess[i].upper()  # Mark correct position in uppercase (like green in Wordle)
                    used_indices.append(i)
        
            # Then, mark letters that are in the word but not in the correct position
            for i in range(WORD_LENGTH):
                if feedback[i] == "_":  # If this position hasn't been marked yet
                    for j in range(WORD_LENGTH):
                        if i != j and guess[i] == target_word[j] and j not in used_indices:
                            feedback[i] = guess[i].lower()  # Mark correct letter, wrong position
                            used_indices.append(j)
                            break
        
            return feedback
        
        # Read the word list and normalize
        with open("c:\\os\\operating systems\\mxes os\\words.txt", "r") as file:
            word_list = [word.strip().lower() for word in file.readlines()]
        
        # Pick a random word
        target_word = random.choice(word_list)
        
        # Game loop
        end = False
        for attempt in range(MAX_GUESSES):
            if end:
                break
            if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("Attempt {attempt + 1}/{MAX_GUESSES}: Enter a 5-letter word (or 'end' to exit): \n> ").strip().lower()
                            engine.runAndWait()
            guess = input(f"> Attempt {attempt + 1}/{MAX_GUESSES}: Enter a 5-letter word (or 'end' to exit): \n> ").strip().lower()
        
            # Check for the exit condition
            if guess == "end":
                end = True
                continue
        
            # Validate input
            if len(guess) != WORD_LENGTH:
                print("> Please enter a 5-letter word.")
                if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("Please enter a 5-letter word.")
                            engine.runAndWait()
                continue
        
            # Get feedback for the guess
            feedback = get_feedback(guess, target_word)
            print("> Feedback:", " ".join(feedback))
            if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("Feedback:", " ".join(feedback))
                            engine.runAndWait()
            # Check if the guess is correct
            if guess == target_word:
                print("> Congratulations! You've guessed the correct word!")
                if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("Congratulations! You've guessed the correct word!")
                            engine.runAndWait()
                break
        
        # If the player didn't guess the word in the given attempts and didn't exit
        if not end and guess != target_word:
            print(f"> Out of attempts! The correct word was '{target_word}'.")
            if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say(f"Out of attempts! The correct word was '{target_word}'.")
                            engine.runAndWait()
    elif program=="money":
        while not end:
            if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("What program do you wish to preform? Add cost .1 Remove cost .2 Add money .3 remove money .4 view report .5 exit .6")
                            engine.runAndWait()
            money_op=input("> What program do you wish to preform?\n> Add cost .1\n> Remove cost .2\n> Add money .3\n> remove money .4\n> view report .5\n> exit .6\n> ")
            if money_op=="1":
                if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("How much money is this cost?")
                            engine.runAndWait()
                cost=input("> How much money is this cost? \n> ")
                with open("c:\\os\\operating systems\\mxes os\\costs","a") as file:
                    file.write(f"{cost}\n")
            if money_op=="2":
                if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("how much cost do you wish to remove?")
                            engine.runAndWait()
                cost_less=int(input("> how much cost do you wish to remove? \n> "))
                with open("c:\\os\\operating systems\\mxes os\\costs","r") as file:
                    costs=file.readlines()
                    costs2=[]
                    costs_len=len(costs)
                    costs_len1=len(costs)
                    while costs_len1>0:
                        f=costs[0]
                        g=f.strip()
                        costs2.append(int(g))
                        costs.pop(0)
                        costs_len1-=1
                    while costs_len-1>0:
                        costs2[0]+=costs2[1]
                        costs2.pop(1)
                        costs_len-=1
                    costs_num=costs2[0]
                    int (costs_num)
                    costs_num-=cost_less
                    with open("c:\\os\\operating systems\\mxes os\\costs","w") as file:
                        file.write(str(costs_num))
            if money_op=="3":
                if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("How much money did you get?")
                            engine.runAndWait()
                pay=input("> How much money did you get? ")
                with open("c:\\os\\operating systems\\mxes os\\money","a") as file:
                    file.write(f"{pay}\n")
            if money_op=="4":
                if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("how much money do you wish to remove?")
                            engine.runAndWait()
                pay_less=int(input("> how much money do you wish to remove? \n> "))
                with open("c:\\os\\operating systems\\mxes os\\money","r") as file:
                    money=file.readlines()
                    money2=[]
                    money_len=len(money)
                    money_len1=len(money)
                    while money_len1>0:
                        f=money[0]
                        g=f.strip()
                        money2.append(int(g))
                        money.pop(0)
                        money_len1-=1
                    while money_len-1>0:
                        money2[0]+=money2[1]
                        money2.pop(1)
                        money_len-=1
                    money_num=money2[0]
                    int (money_num)
                    money_num-=pay_less
                    with open("c:\\os\\operating systems\\mxes os\\money","w") as file:
                        file.write(f"{str(money_num)}\n")
            if money_op=="5":
                with open("c:\\os\\operating systems\\mxes os\\money","r") as file:
                    money=file.readlines()
                    money2=[]
                    money_len=len(money)
                    money_len1=len(money)
                    while money_len1>0:
                        f=money[0]
                        g=f.strip()
                        money2.append(int(g))
                        money.pop(0)
                        money_len1-=1
                    while money_len-1>0:
                        money2[0]+=money2[1]
                        money2.pop(1)
                        money_len-=1
                    money_num=money2[0]
                    with open("c:\\os\\operating systems\\mxes os\\money","w") as file:
                        file.write(f"{str(money_num)}\n")
                with open("c:\\os\\operating systems\\mxes os\\costs","r") as file:
                    costs=file.readlines()
                    costs2=[]
                    costs_len=len(costs)
                    costs_len1=len(costs)
                    while costs_len1>0:
                        f=costs[0]
                        g=f.strip()
                        costs2.append(int(g))
                        costs.pop(0)
                        costs_len1-=1
                    while costs_len-1>0:
                        costs2[0]+=costs2[1]
                        costs2.pop(1)
                        costs_len-=1
                    costs_num=costs2[0]
                    with open("c:\\os\\operating systems\\mxes os\\costs","w") as file:
                        file.write(str(costs_num))
                        if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say(f"You have {money_num} dollars.\n> You spent {costs_num} dollars.")
                            engine.runAndWait()
                print(f"> You have {money_num} dollars.\n> You spent {costs_num} dollars.")
                tot_money=money_num-costs_num
                if tot_money<=0:
                    if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say(f"You have {tot_money} dollars")
                            engine.runAndWait()
                    print(f"\033[1;31;48m> You have {tot_money} dollars =({ansi_escape}")
                if tot_money>0:
                    if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say(f"You have {tot_money} dollars")
                            engine.runAndWait()
                    print(f"\033[1;32;48m> You have {tot_money} dollars =){ansi_escape}")
            if money_op=="6":
                end=True
    elif program=="version finder":
        while not end:
            if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("How meny characters are in the code?")
                            engine.runAndWait()
            code_len=int(input("> How meny characters are in the code?\n> "))
            unedited_version=code_len*.00002
            multiple=.000001
            def round_to_nearest(unedited_version, multiple):
                if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say(round(unedited_version / multiple) * multiple)
                            engine.runAndWait()
                return round(unedited_version / multiple) * multiple
            rounded_value = round_to_nearest(unedited_version, multiple)  # Expected output: 23000
            if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say("v",rounded_value)
                            engine.runAndWait()
            print("> v",rounded_value)
            end=True
    if end==True:
        end=False
        program="standby"
    if program not in keywords:
        print(f"> {program} is not a valid program")
        if tts_mode=="t":
                            engine = pyttsx3.init()
                            engine.say(f"{program} is not a valid program")
                            engine.runAndWait()
        program="standby"
