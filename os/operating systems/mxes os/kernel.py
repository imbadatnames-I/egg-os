import os
import shutil
if os.path.exists("c:\\os\\operating systems\\mxes os\\program.py"):
    with open("c:\\os\\operating systems\\mxes os\\program.py") as program:
        program = program.read()
        exec(program)
else:
    print("there is no program file")
    print("fixing")
    if os.path.exists("C:\\os_rec\\mxes os\\startup.py"):
        shutil.move("C:\\os_rec\\mxes os\\startup.py","C:\\os\\operating systems\\mxes os")
        shutil.copyfile("C:\\os\\operating systems\\mxes os\\startup.py","C:\\os_rec\\mxes os\\startup.py")
        print("fixed")