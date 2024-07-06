import shutil
import os
program="version imp"
if program=="version imp":
    old_versions_len=os.listdir("C:\\Users\\Student\\Desktop\\old mxes os versions")
    print("> old mxes os versions:")
    while len(old_versions_len)>0:
        old_versions_1=old_versions_len[0]
        print(">",old_versions_1)
        old_versions_len.pop(0)
    source_folder = "C:\\Users\\Student\\Desktop\\old mxes os versions"
    destination_folder = "c:\\Users\\Student\\Desktop\\mxes os"
    os.makedirs(destination_folder, exist_ok=True)
    file_name = input("> What is the name of the file you want to open warning some old versions have bugs.\n> ")
    try:
        source_file_path = os.path.join(source_folder, file_name)
        destination_file_path = destination_folder
        shutil.move(source_file_path, destination_file_path)
        print(f"> Moved {file_name} from {source_folder} to {destination_folder}")
    except:
        print("> There was a error it's most likely that the file you tryed to open doesn't exist.")
if program=="version open":
    file_name=input("> What is the name of the file you want to open?\n> ")
    with open(file_name) as f:
        code = f.read()
        exec(code)