import time
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
username, password, hint, max_guesses,permission_level,tts_mode = user_info
print("> Input journal entry. Type '$next$' to create a new entry, '$end$' to exit, or '$view$' to see previous entries\n> ")
if tts_mode=="t":
    engine.say("Input journal entry. Type '$next$' to create a new entry, '$end$' to exit, or '$view$' to see previous entries")
    engine.runAndWait()
while not end:
    journal_input = input("> ")
    current_time_utc = time.gmtime()  # Get current time in UTC
    current_time_cst = time.localtime(time.mktime(current_time_utc) - (6 * 3600))  # Subtract 5 hours for CST
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
                engine.say("Journal Entries")
                engine.runAndWait()
            print(f"{full_journal}")
            if tts_mode=="t":
                engine.say(full_journal)
                engine.runAndWait()
        except FileNotFoundError:
            print("> No journal entries found.")
            if tts_mode=="t":
                engine.say("No journal entries found")
                engine.runAndWait()
    elif journal_input == "$next$":
        # Save the current entry and start a new one
        if current_entry:
            with open("c:\\os\\operating systems\\mxes os\\journal", "a") as file:
                file.write(f"> {current_time}:\n" + "\n".join(current_entry) + "\n\n")
                current_entry=[]
    else:
        # Append the user input to the current entry list
        current_entry.append(journal_input)