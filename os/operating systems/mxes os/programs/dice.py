
import random
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
if tts_mode=="t":
    engine.say("how many sides do these dice have? To leave type end.")
    engine.runAndWait()
dice_sides_number=input("> how many sides do these dice have? To leave type end. \n> ")
if dice_sides_number.lower()=="end":
        end=True
else:
    if tts_mode=="t":
        engine.say("How meny dice are there?")
        engine.runAndWait()
    number_of_dice=input("> How meny dice are there?\n> ")
    dice_number_pr=1
    while number_of_dice>0:
            dice_number=random.randint(1,dice_sides_number)
            if tts_mode=="t":
                engine.say(f"die {dice_number_pr} number is {dice_number}")
                engine.runAndWait()
            print(f"> die {dice_number_pr} number is {dice_number}")
            dice_number_pr+=1
            number_of_dice-=1