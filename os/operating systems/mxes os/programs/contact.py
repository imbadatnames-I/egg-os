import time
import os
import pyttsx3 # type: ignore
engine = pyttsx3.init()
def get_user_info():
                    if os.path.exists("c:\\operating systems\\mxes os\\user_info.txt"):
                        with open("c:\\operating systems\\mxes os\\user_info.txt", "r") as file:
                            lines = file.readlines()
                            return lines
                    return None
user_info = get_user_info()
username, password, hint, max_guesses,permission_level,tts_mode = user_info
def add_name():
        if tts_mode=="t":
            engine.say("What is the name of the person?")
            engine.runAndWait()
        contact_name = input("> What is the name of the person? \n> ")
        if tts_mode=="t":
            engine.say("What is what is their phone number?")
            engine.runAndWait()
        contact_phone = input("> What is what is their phone number?\n> ")
        if tts_mode=="t":
            engine.say("What is what is their address?")
            engine.runAndWait()
        contact_address = input("> What is what is their address?\n> ")
        with open("c:\\operating systems\\mxes os\\contact.txt", "a") as file:
    # Check if the file is empty
            file.seek(0, 2)  # Move to the end of the file
            if file.tell() != 0:  # If file is not empty
                file.write("\n")  # Add newline if not the first task
                file.write(f"name: {contact_name}, phone number: {contact_phone}\nAddress: {contact_address}\n")
def delete_contact():
        if tts_mode=="t":
            engine.say(f"What is the name of the contact you want to delete?")
            engine.runAndWait()
        del_task = input("> What is the name of the contact you want to delete? \n> ")
        with open("c:\\operating systems\\mxes os\\contact.txt", "r") as file:
            lines = file.readlines()  # Read all lines from the file
        with open("c:\\operating systems\\mxes os\\contact.txt", "w") as file:
            contact_deleted = False
            i = 0
            while i < len(lines):
                if f"name: {del_task}" in lines[i]:
                    task_deleted = True
                    # Skip current line (task name and state) and the next two lines
                    i += 3
                else:
                    file.write(lines[i])
                    i += 1
            if task_deleted:
                print("> contact deleted successfully.")
                if tts_mode=="t":
                    engine.say(f"contact deleted successfully.")
                    engine.runAndWait()
            else:
                print("> contact not found.")
                if tts_mode=="t":
                    engine.say(f"contact not found")
                    engine.runAndWait()
def view_contact():
    with open("c:\\operating systems\\mxes os\\contact.txt", "r") as file:
        contacts = file.readlines()
    for contact in contacts:
        print(contact.strip())  # Strip to remove newline character
        if tts_mode=="t":
            engine.say(contact.strip())
            engine.runAndWait()
while not end:
        if tts_mode=="t":
            engine.say("Do you want to add, delete, view contacts, or end program?")
            engine.runAndWait()
        operation = input("> Do you want to add, delete, or view contacts, or end program? \n> ")
        if operation == "end":
            end=True
        elif operation == "add":
            add_name()
        elif operation == "delete":
            delete_contact()
        elif operation == "view":
            view_contact()
        else:
            print("> Invalid operation. Please try again.")
            if tts_mode=="t":
                engine.say(f"Invalid operation. Please try again.")
                engine.runAndWait()