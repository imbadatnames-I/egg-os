import os
import pyttsx3 # type: ignore
engine = pyttsx3.init()
def get_user_info():
                    if os.path.exists("c:\\os\\operating systems\\mxes os\\user_info.txt"):
                        with open("c:\\os\\operating systems\\mxes os\\user_info.txt", "r") as file:
                            lines = file.readlines()
                            return lines
                    return None
user_info = get_user_info()
tts_mode = user_info[5]
end=False
def read_passwords():
    with open("c:\\os\\operating systems\\mxes os\\password_list.txt", "r") as file:
        return file.readlines()    
def write_passwords(lines):
    with open("c:\\os\\operating systems\\mxes os\\password_list.txt", "w") as file:
        file.writelines(lines)
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