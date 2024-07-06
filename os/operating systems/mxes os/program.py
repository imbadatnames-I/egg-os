running=True # sets running to true
os_file="Mxes OS® v 1.03.65.75.py"
version="1.00.00.0"
ansi_escape = "\033[1;32;48m"
keywords=["shutdown","standby","startup","help"]
program="startup"
import pyttsx3 # type: ignore
engine = pyttsx3.init()
end=False
program=="startup"
expected_system_files = {"blank.wav","mxes os startup.wav", os_file,".vscode",".venv","__pycache__","words.txt","Mxes OS (R) Version 0.22.15.6.py","Mxes OS® Version 0.14.78.8.py","Mxes OS® Version 0.22.15.6.py","Mxes OS® Version 0.41.32.8.py","Mxes OS® Version 0.42.43.6.py","Mxes OS® Version 0.42.92.8.py","Mxes OS® Version 0.48.13.4.py","Mxes OS® Version 0.48.60.6.py","Mxes OS® Version 0.52.58.8.py","Mxes OS® Version 0.58.30.8.py","Mxes OS® Version 0.97.15.6.py","Mxes OS® Version 1.10.16.2.py","trap.py","timers","time","tasks.txt","size.py","Mxes OS® Version 1.00.py","extensions","e.py","alarm.wav"}
while running==True:
        import os
        import hashlib
        import time
        from datetime import datetime
        from typing import List
        import winsound
        import base64 
        import psutil
        battery = psutil.sensors_battery()
        if program=="startup":
                winsound.PlaySound("C:\\os\\operating systems\\mxes os\\startup.wav", winsound.SND_ASYNC)
                if os.path.exists("C:\\os\\operating systems\\mxes os\\user_info.txt"):
                        with open("C:\\os\\operating systems\\mxes os\\user_info.txt", "r") as file:
                            lines = file.readlines()
                            user_info=lines
                            username, password, hint, max_guesses,permission_level,tts_mode = user_info
                def save_user_info(username, password, hint, max_guesses, permission_level, tts_mode):
                    with open("C:\\os\\operating systems\\mxes os\\user_info.txt", "w") as file:
                        file.write(f"{username}\n{password}\n{hint}\n{max_guesses}\n{permission_level}\n{tts_mode}")
                def authenticate(username, password, hint, max_guesses,permission_level,tts_mode,ansi_escape,hashlib):
                        if int(permission_level.strip())==0:
                            print(f"{ansi_escape}> invalid copy of mxes os exiting")
                            exit()
                        attempts = 0
                        locked_time = 15
                        while attempts < int(max_guesses):
                            if tts_mode=="t":
                                    time.sleep(2)
                                    engine.say(f"Hello {username} please enter your password:")
                                    engine.runAndWait()
                            guess=input(f"{ansi_escape}> Hello {username} please enter your password:\n> ")
                            if hashlib.sha256(guess.encode()).hexdigest() == password:
                                print("> Authentication successful!")
                                if tts_mode=="t":
                                    engine.say("Authentication successful!")
                                    engine.runAndWait()
                                return True
                            else:
                                attempts += 1
                                print("> Incorrect password.")
                                if tts_mode=="t":
                                    engine.say("Incorrect password")
                                    engine.runAndWait()
                                if attempts == 1:
                                    print("> Hint:", hint)
                                    if tts_mode=="t":
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
                if user_info:
                    username, password, hint, max_guesses,permission_level,tts_mode = user_info
                    if authenticate(username.strip(), password.strip(), hint.strip(), max_guesses.strip(),permission_level.strip(),tts_mode.strip(),ansi_escape,hashlib):
                        # Continue with authenticated user
                        pass
                    else:
                        if tts_mode=="t":
                            engine.say(f"Authentication failed")
                            engine.runAndWait()
                        print("> Authentication failed.")
                        exit()
                else:
                    print("\033[1;32;48m> Welcome to the Mxes OS®!")
                    username = input("> What do you want to name your account? ")
                    password = hashlib.sha256(input("> Please enter your password: ").encode()).hexdigest()
                    hint = input("> What is the password hint? ")
                    max_guesses = input("> How many wrong guesses until guesses are frozen for a duration? ")
                    tts_mode=input("> Do you want tts? t/f\n> ")
                    admin_code=int(input("> What is your mxes os code?\n> "))
                    if admin_code==3035189:
                        permission_level="1"
                    else:
                        permission_level="0"
                        print(f"{ansi_escape}> invalid copy of mxes os exiting")
                        exit()
                    save_user_info(username, password, hint, max_guesses,permission_level,tts_mode)
                    print("> Account created successfully!")
                print(">                                                                              _ __ ___ __  _____  ___     ___  ___ ")
                print(">                                                                             | '_ ` _ /\ \/ / _ \/ __|   / _ \/ __|")
                print(">                                                                             | | | | | |>  <  __/\__ \  | (_) \__ \ ")
                print(">                                                                             |_| |_| |_/_/\_\___||___/   \___/|___/")
                print(">                                                                             ")
                print(">                                                                             ")
                print(">                                                                             ")
                print(f">                                                                             Stir Stick® Mxes OS® Version {version}")
                print(f">                                                                                   ©Stir Stick Corp 2024-{datetime.now().year}")
                print(">                                                                                     press enter to start")
                print("> ")
                print("> ")
                print("> ")
                if tts_mode=="t":
                    engine.say("press enter to start")
                    engine.runAndWait()
                input("> ")
                end=False
                program="standby"
                print ("> input help for a list of all programs.")
                if tts_mode=="t":
                    engine.say("input help for a list of all programs.")
                    engine.runAndWait()
        elif program=="standby":
                if tts_mode=="t":
                    engine.say("what program do you want to run?")
                    engine.runAndWait()
                print(f"> is plugged: {battery.power_plugged} charge: {battery.percent} aprox secs left: {battery.secsleft}")
                current_time_utc = time.gmtime()  # Get current time in UTC
                current_time_cst = time.localtime(time.mktime(current_time_utc) - (6 * 3600))  # Subtract 5 hours for CST
                formatted_time=time.strftime("%Y-%m-%d %H:%M:%S", current_time_cst)
                print(f"> time: {formatted_time}")
                program=input("> what program do you want to run? \n> ")
                program_bytes = program.encode("ascii") 
                base64_bytes = base64.b64encode(program_bytes) 
                base64_string = base64_bytes.decode("ascii") 
        elif program=="shutdown": 
                while end==False:
                    if tts_mode=="t":
                                engine.say(f"Mxes OS® is shutting down are you sure? t/f")
                                engine.runAndWait()
                    shutdown_confirmation=input("> Mxes OS® is shutting down are you sure? t/f \n> ")
                    if shutdown_confirmation=="t":
                        running=False
                        print ("> shutting down Mxes OS®")
                        if tts_mode=="t":
                                engine.say(f"shutting down Mxes OS®")
                                engine.runAndWait()
                        break
                    elif shutdown_confirmation=="f":
                        print("> shutdown stopped")
                        if tts_mode=="t":
                            engine.say(f"shutdown stopped")
                            engine.runAndWait()
                            program="standby"
                    else:
                        print("> Invalid input")
                        if tts_mode=="t":
                                engine.say(f"Invalid input")
                                engine.runAndWait()
                    end=True
        elif program=="help":
            with open("c:\\os\\operating systems\mxes os\program","r") as file:
                programs=file.readlines()
            while len(programs)>0:
                print(f">    {programs[0].strip()}")
                programs.pop(0)
            end=True
        if program not in keywords:
            if os.path.exists(f"c:\\os\\operating systems\\mxes os\\programs\\{program}.py"):
                with open(f"c:\\os\\operating systems\\mxes os\\programs\\{program}.py") as program:
                    program = program.read()
                    exec(program)
            else:
                print("> That program doesn't exist.")
            end=True
        if end==True:
            program="standby"
            end=False