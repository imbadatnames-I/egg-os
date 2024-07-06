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
with open ("colour","w") as colour:
    colour.write(ansi_escape)

print(f"> {ansi_escape}This is styled text.")  # Reset at the end to avoid affecting further output
end=True