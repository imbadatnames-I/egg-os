import os
import pyttsx3 # type: ignore
engine = pyttsx3.init()
def get_user_info():
                    if os.path.exists("c:\\operating systems\\mxes os\\user_info.txt"):
                        with open("c:\\operating systems\\mxes os\\c:\\operating systems\\mxes os\\user_info.txt", "r") as file:
                            lines = file.readlines()
                            return lines
                    return None
user_info = get_user_info()
username, password, hint, max_guesses,permission_level,tts_mode = user_info
while not end:
    if tts_mode=="t":
        engine.say("What program do you wish to preform? Add cost .1 Remove cost .2 Add money .3 remove money .4 view report .5 exit .6")
        engine.runAndWait()
    money_op=input("> What program do you wish to preform?\n> Add cost .1\n> Remove cost .2\n> Add money .3\n> remove money .4\n> view report .5\n> exit .6\n> ")
    if money_op=="1":
        if tts_mode=="t":
            engine.say("How much money is this cost?")
            engine.runAndWait()
        cost=input("> How much money is this cost? \n> ")
        with open("c:\\operating systems\\mxes os\\c:\\operating systems\\mxes os\\costs","a") as file:
            file.write(f"{cost}\n")
    if money_op=="2":
        if tts_mode=="t":
            engine.say("how much cost do you wish to remove?")
            engine.runAndWait()
        cost_less=int(input("> how much cost do you wish to remove? \n> "))
        with open("c:\\operating systems\\mxes os\\c:\\operating systems\\mxes os\\costs","r") as file:
            costs=file.readlines()
            costs2=[]
            costs_len=len(costs)
            costs_len1=len(costs)
            while costs_len1>0:
                f=costs[0]
                g=f.strip()
                costs2.append(int(g))
                costs.pop(0)
                costs_len1-=1
            while costs_len-1>0:
                costs2[0]+=costs2[1]
                costs2.pop(1)
                costs_len-=1
            costs_num=costs2[0]
            int (costs_num)
            costs_num-=cost_less
            with open("c:\\operating systems\\mxes os\\costs","w") as file:
                file.write(str(costs_num))
    if money_op=="3":
        if tts_mode=="t":
            engine.say("How much money did you get?")
            engine.runAndWait()
        pay=input("> How much money did you get? ")
        with open("c:\\operating systems\\mxes os\\money","a") as file:
            file.write(f"{pay}\n")
    if money_op=="4":
        if tts_mode=="t":
            engine.say("how much money do you wish to remove?")
            engine.runAndWait()
        pay_less=int(input("> how much money do you wish to remove? \n> "))
        with open("c:\\operating systems\\mxes os\\money","r") as file:
            money=file.readlines()
            money2=[]
            money_len=len(money)
            money_len1=len(money)
            while money_len1>0:
                f=money[0]
                g=f.strip()
                money2.append(int(g))
                money.pop(0)
                money_len1-=1
            while money_len-1>0:
                money2[0]+=money2[1]
                money2.pop(1)
                money_len-=1
            money_num=money2[0]
            int (money_num)
            money_num-=pay_less
            with open("c:\\operating systems\\mxes os\\money","w") as file:
                file.write(f"{str(money_num)}\n")
    if money_op=="5":
        with open("c:\\operating systems\\mxes os\\money","r") as file:
            money=file.readlines()
            money2=[]
            money_len=len(money)
            money_len1=len(money)
            while money_len1>0:
                f=money[0]
                g=f.strip()
                money2.append(int(g))
                money.pop(0)
                money_len1-=1
            while money_len-1>0:
                money2[0]+=money2[1]
                money2.pop(1)
                money_len-=1
            money_num=money2[0]
            with open("c:\\operating systems\\mxes os\\money","w") as file:
                file.write(f"{str(money_num)}\n")
        with open("c:\\operating systems\\mxes os\\costs","r") as file:
            costs=file.readlines()
            costs2=[]
            costs_len=len(costs)
            costs_len1=len(costs)
            while costs_len1>0:
                f=costs[0]
                g=f.strip()
                costs2.append(int(g))
                costs.pop(0)
                costs_len1-=1
            while costs_len-1>0:
                costs2[0]+=costs2[1]
                costs2.pop(1)
                costs_len-=1
            costs_num=costs2[0]
            with open("c:\\operating systems\\mxes os\\costs","w") as file:
                file.write(str(costs_num))
                if tts_mode=="t":
                    engine.say(f"You have {money_num} dollars.\n> You spent {costs_num} dollars.")
                    engine.runAndWait()
        print(f"> You have {money_num} dollars.\n> You spent {costs_num} dollars.")
        tot_money=money_num-costs_num
        if tot_money<=0:
            if tts_mode=="t":
                engine.say(f"You have {tot_money} dollars")
                engine.runAndWait()
            print(f"\033[1;31;48m> You have {tot_money} dollars =(\033[1;32;48m")
        if tot_money>0:
            if tts_mode=="t":
                engine.say(f"You have {tot_money} dollars")
                engine.runAndWait()
            print(f"\033[1;32;48m> You have {tot_money} dollars =)\033[1;32;48m")
    if money_op=="6":
        end=True