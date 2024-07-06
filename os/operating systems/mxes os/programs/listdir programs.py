import os
while True:
    op=input("> do you want to see the info for os, operating systems, mxes os, programs, or exit?\n> ")
    if op=="programs":
        programs=os.listdir("c:\\os\\operating systems\\mxes os\\programs")
        programs2=programs
        programs_size=[]
        while len(programs2)>0:
            if ".py" in programs2[0]:
                programs_size.append(os.path.getsize(f"C:\\os\\operating systems\\mxes os\\programs\\{programs2[0].strip()}"))
            programs2.pop(0)
        programs=os.listdir("c:\\os\\operating systems\\mxes os\\programs")
        while len(programs)>0:
            if ".py" in programs[0]:
                print(programs[0])
            programs.pop(0)
        while len(programs_size)>0:
            print(programs_size[0])
            programs_size.pop(0)
    if op=="os":
        programs=os.listdir("c:\\os")
        programs2=programs
        programs_size=[]
        while len(programs2)>0:
            if ".py" in programs2[0]:
                programs_size.append(os.path.getsize(f"C:\\os\\{programs2[0].strip()}"))
            programs2.pop(0)
        programs=os.listdir("c:\\os")
        while len(programs)>0:
            if ".py" in programs[0]:
                print(programs[0])
            programs.pop(0)
        while len(programs_size)>0:
            print(programs_size[0])
            programs_size.pop(0)
    if op=="mxes os":
        programs=os.listdir("c:\\os\\operating systems\\mxes os")
        programs2=programs
        programs_size=[]
        while len(programs2)>0:
            if ".py" in programs2[0]:
                programs_size.append(os.path.getsize(f"C:\\os\\operating systems\\mxes os\\{programs2[0].strip()}"))
            programs2.pop(0)
        programs=os.listdir("c:\\os\\operating systems\\mxes os")
        while len(programs)>0:
            if ".py" in programs[0]:
                print(programs[0])
            programs.pop(0)
        while len(programs_size)>0:
            print(programs_size[0])
            programs_size.pop(0)