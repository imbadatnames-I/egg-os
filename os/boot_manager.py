import os
import shutil
number_of_operating_systems=len(os.listdir("c:\\os\\operating systems"))
operating_systems=os.listdir("c:\\os\\operating systems")
print(f"\033[1;32;48m> number of operating systems: {number_of_operating_systems}")
if number_of_operating_systems>1:
    print(f"> operating systems: {operating_systems}")
    operating_system=input("> what os do you wish to boot? ")
if number_of_operating_systems==1:
    operating_system=operating_systems[0]
if os.path.exists(f"c:\\os\\operating systems\\{operating_system}\\kernel.py"):
    with open(f"c:\\os\\operating systems\\{operating_system}\\kernel.py") as kernel:
        kernel = kernel.read()
        exec(kernel)
else:
    print("there is no kernel installed")
    print("fixing")
    if os.path.exists(f"C:\\os_rec\\{operating_system}\\kernel.py"):
        shutil.move(f"C:\\os_rec\\{operating_system}\\kernel.py",f"C:\\os\\operating systems\\{operating_system}")
        shutil.copyfile(f"C:\\os\\operating systems\\{operating_system}\\kernel.py",f"C:\\os_rec\\{operating_system}\\kernel.py")
        print("fixed")
        with open(f"c:\\os\\operating systems\\{operating_system}\\kernel.py") as kernel:
            kernel = kernel.read()
            exec(kernel)
programs=os.listdir("c:\\os\\operating systems\\mxes os\\programs")
while len(programs)>0:
    print(programs[0])
    programs.pop(0)