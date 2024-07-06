expected_system_files = {"blank.wav","mxes os startup.wav",".vscode",".venv","__pycache__","words.txt","Mxes OS (R) Version 0.22.15.6.py","Mxes OS® Version 0.14.78.8.py","Mxes OS® Version 0.22.15.6.py","Mxes OS® Version 0.41.32.8.py","Mxes OS® Version 0.42.43.6.py","Mxes OS® Version 0.42.92.8.py","Mxes OS® Version 0.48.13.4.py","Mxes OS® Version 0.48.60.6.py","Mxes OS® Version 0.52.58.8.py","Mxes OS® Version 0.58.30.8.py","Mxes OS® Version 0.97.15.6.py","Mxes OS® Version 1.10.16.2.py","trap.py","timers","time","tasks.txt","size.py","Mxes OS® Version 1.00.py","extensions","e.py","alarm.wav"}
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
file_op=input("> Do you wish to rename a file, delete a file, or exit.\n> ")
if file_op.lower()=="delete":
   file_list = os.listdir("c:\\Users\\Student\\Desktop\\mxes os")
   system_files = []
   user_files = []
   while file_list:
       file_name = file_list.pop(0)
       if file_name in expected_system_files:
           system_files.append(file_name)
       else:
           user_files.append(file_name)
   print("> Other Files:", user_files)
   print("> System Files:", system_files)
   deleted_file=input("> What is the name of the file you wish to delete you can't delete system files to exit input something that is not a user file.\n> ")
   if deleted_file in user_files:
       os.remove(f"c:\\os\\operating systems\\mxes os\\{deleted_file}")
if file_op.lower()=="rename":
   file_list = os.listdir("c:\\Users\\Student\\Desktop\\mxes os")
   system_files = []
   user_files = []
   while file_list:
       file_name = file_list.pop(0)
       if file_name in expected_system_files:
           system_files.append(file_name)
       else:
           user_files.append(file_name)
   print("> Other Files:", user_files)
   print("> System Files:", system_files)
   file_name=input("> What is the name of the file you wish to rename.\n> ")
   file_new_name=input(f"> What do you wish to rename {file_name}.\n> ")
   os.rename(f"c:\\os\\operating systems\\mxes os\\{file_name}",f"c:\\os\\operating systems\\mxes os\\{file_new_name}")
if file_op.lower()=="exit":
    exit()