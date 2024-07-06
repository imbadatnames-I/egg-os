count=0
count2=0
inpt=input("what line do you want to look at?\n")
import os
programs=os.listdir("c:\\os\\operating systems\\mxes os\\programs")
programs.pop(len(programs)-1)
while len(programs)>0:
    with open(f"c:\\os\\operating systems\\mxes os\\programs\\{programs[0]}") as file:
            e=file.readlines()
    while len(e)>0:
        if inpt in e[0].strip():
            count+=1
        e.pop(0)
    print (programs[0])
    print(count)
    count2+=count
    count=0
    print()
    programs.pop(0)
print(count2)