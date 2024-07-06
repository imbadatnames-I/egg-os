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
end=False
if end==False:
    txt_name = input("> What is the name of your document? \n> ")
    if tts_mode=="t":
                engine.say(f"What is the name of your document?")
                engine.runAndWait()
    print("> ")
    txt_op="write"
while not end:
    if txt_op=="view":
        with open(f"{txt_name}.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                print(f"> {line.strip()}")
                txt_op = "write"
                if tts_mode=="t":
                    engine.say(line.strip())
                    engine.runAndWait()
                txt_op="write"
    if txt_op == "write":
        inpt=input("> ")
        if inpt=="[edit]":
            txt_op="edit"
        if inpt=="[write]":
            txt_op=="write"
        if inpt=="[view]":
            txt_op="view"
        if inpt == "[end]":
            end = True
            txt_op="end"
        if txt_op == "write":
            with open(f"{txt_name}.txt", "a") as file:
                file.seek(0, 2)  # Move to the end of the file
                file.write(inpt)
                file.write("\n")  # Write user input to the file
    elif txt_op == "edit":
        old_line = int(input("> What line is being edited? \n> ")) - 1  # Adjust to 0-indexed line number
        if tts_mode=="t":
                engine.say(f"What line is being edited")
                engine.runAndWait()
        with open(f"{txt_name}.txt", "r") as file:
            lines = file.readlines()
        if old_line==-1:
            end=True
        if old_line < -1 or old_line >= len(lines):
            print("> Invalid line number.")
            if tts_mode=="t":
                engine.say(f"Invalid line number")
                engine.runAndWait()
        elif old_line>-1:
            old_content = lines[old_line].strip()  # Get the content of the old line
            new_content = input(f"> Current content: {old_content}\n> New content: \n> ")  # Prompt for new content
            if tts_mode=="t":
                engine.say(f"current content: {old_content}\nNew content:")
                engine.runAndWait()
            with open(f"{txt_name}.txt", "r") as file:
                lines = file.readlines()
                lines[old_line] = f"{new_content}\n"
            with open(f"{txt_name}.txt", "w") as file:
                file.writelines(lines)
                txt_op="view"