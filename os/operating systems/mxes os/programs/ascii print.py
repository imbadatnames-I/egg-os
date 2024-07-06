print("> input the ascii art line by line. ")
ascii=[]
inputt=input("> input line to exit input $end$.\n> ")
ascii.append(inputt)
while inputt.lower()!="$end$":
    inputt=input("> ")
    ascii.append(inputt)
ascii.pop(len(ascii)-1)
print_mode=input("> do you want there to be 78 or 0 spaces input 0 or 78\n> ")
if print_mode=="0":
    while len(ascii)>0:
        print(f'print("{ascii[0]}")')
        ascii.pop(0)
if print_mode=="78":
    while len(ascii)>0:
        print(f'print("                                                                              {ascii[0]}")')
        ascii.pop(0)
input()