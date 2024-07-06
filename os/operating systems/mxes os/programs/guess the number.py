import random
z=0
import os
import pyttsx3 # type: ignore
engine = pyttsx3.init()
def get_user_info():
                    if os.path.exists(f"c:\\os\\operating systems\\mxes os\\user_info.txt"):
                        with open("c:\\os\\operating systems\\mxes os\\user_info.txt", "r") as file:
                            lines = file.readlines()
                            return lines
                    return None
user_info = get_user_info()
username, password, hint, max_guesses,permission_level,tts_mode = user_info
while not end:
    print ("> how meny guesses do you want\n> ")
    if tts_mode=="t":
        engine.say("how meny guesses do you want")
        engine.runAndWait()
    guesses=int(input("> "))+1
    guesses=guesses-1
    print("> how big is the range use 1 number\n> ")
    if tts_mode=="t":
        engine.say("how big is the range use 1 number")
        engine.runAndWait()
    y=int(input("> "))
    number=random.randint(1,y)
    while guesses>0:
        if tts_mode=="t":
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
                    engine.say(f"you got it right and the number is,{number}")
                    engine.runAndWait()
                print ('you got it right and the number is',number)
                if tts_mode=="t":
                    engine.say('it took',z+1,'attempts for you to find the number',number,"you had",guesses,"guesses left")
                    engine.runAndWait()
                print ('it took',z+1,'attempts for you to find the number',number,"you had",guesses,"guesses left")
                if tts_mode=="t":
                    engine.say("how meny guesses do you want?")
                    engine.runAndWait()
                guesses=int(input("> how meny guesses do you want? \n> "))+1
                if tts_mode=="t":
                    engine.say("how big is the range use 1 number")
                    engine.runAndWait()
                y=int(input("> how big is the range use 1 number\n> "))
                number=random.randint(1,y)
                end=True