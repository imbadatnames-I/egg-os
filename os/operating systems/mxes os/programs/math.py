import re
import os
import pyttsx3 # type: ignore
engine = pyttsx3.init()
def get_user_info():
                    if os.path.exists("c:\\operating systems\\mxes os\\user_info.txt"):
                        with open("c:\\os\\operating systems\\mxes os\\user_info.txt", "r") as file:
                            lines = file.readlines()
                            return lines
                    return None
user_info = get_user_info()
tts_mode="f"
end=False
def calculate(expression):
    valid_characters = re.match(r"^[d0-9+\-*/n().e\s]+$", expression)
    if not valid_characters:
        if tts_mode=="t":
                engine.say("Error: Invalid characters in expression.")
                engine.runAndWait()
        return "Error: Invalid characters in expression."
    try:
        result = eval(expression)
        return result
    except Exception as e:
        if tts_mode=="t":
                engine.say(f"Error: {e}")
                engine.runAndWait()
        return f"Error: {e}"
while not end:
    if tts_mode=="t":
                    engine.say("Enter a mathematical expression:")
                    engine.runAndWait()
    expression = input("> Enter a mathematical expression: \n> ")
    if expression=="end":
        end=True
    result = calculate(expression)
    if tts_mode=="t":
                    engine.say("Result:", result)
                    engine.runAndWait()
    print("> Result:", result)
