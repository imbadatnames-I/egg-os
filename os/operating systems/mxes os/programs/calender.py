import time
n=1
nextt=False
current_time_utc = time.gmtime()  # Get current time in UTC
current_time_cst = time.localtime(time.mktime(current_time_utc) - (6 * 3600))  # Subtract 5 hours for CST
time=time.strftime("%d\%m\%y", current_time_cst)
while True:
    if nextt==True:
        calen_input="view"
    calen_input=input("> Do you want to view the days events add a event or remove a event/task or end program. commands are add, remove, view, and end\n> ")
    if calen_input.lower()=="end":
        print("> exiting")
        exit()
    if calen_input=="add":
        title=input("> What is the title of the event/task?\n> ")
        date=input("> what is the date of the event/task? use the dd\mm\yy format\n> ")
        priority=input("> What is the priority level of the event/task\n> ")
        desc=input("> write the description in the line below and when done press enter.\n> ")
        repeat=input("> do you want to repeat it every\n> 1. day\n> 2. week\n> 3. month\n> 4. year\n> 5. none")
        with open("c:\\os\\operating systems\\mxes os\\calender", "a") as file:
            file.seek(0, 2)  # Move to the end of the file
            if file.tell() != 0:  # If file is not empty
                file.write("\n")  # Add newline if not the first task
            file.write(f"{date}   {current_time_cst.tm_yday}\n{title}\n{desc}\n{priority}\n{repeat}\n")
    if calen_input=="view":
        with open("c:\\os\\operating systems\\mxes os\\calender","r") as file:
            calender=file.readlines()
        if len(calender)>2:
            nextt=False
            print(f"> date: {time}\n> ")
            while len(calender)>0:
                    if calender[0].strip()==time:
                        print(f"> {calender[0].strip()}")
                        calender.pop(0)
                        print(f"> {calender[0].strip()}")
                        calender.pop(0)
                        print(f"> {calender[0].strip()}")
                        calender.pop(0)
                        print(f"> {calender[0].strip()}")
                        calender.pop(0)
                        if len(calender)>0:
                            print(f"> {calender[0].strip()}")
                            calender.pop(0)
                    else:
                                            if len(calender)>0:
                                                if calender[4].strip()=="5":
                                                    calender.pop(0)
                                                    calender.pop(0)
                                                    calender.pop(0)
                                                    calender.pop(0)
                                                    calender.pop(0)
                                                    if len(calender)>0:
                                                        calender.pop(0)
                                            if len(calender)>0:
                                                if calender[4].strip()=="4":
                                                    if calender[0][:5]==date_after_month[:5]:
                                                        e=True
                                                        print(f"> {calender[0].strip()}")
                                                        calender.pop(0)
                                                        print(f"> {calender[0].strip()}")
                                                        calender.pop(0)
                                                        print(f"> {calender[0].strip()}")
                                                        calender.pop(0)
                                                        print(f"> {calender[0].strip()}")
                                                        calender.pop(0)
                                                        if len(calender)>0:
                                                            print(f"> {calender[0].strip()}")
                                                            calender.pop(0)
                                            if len(calender)>0:
                                                if calender[4].strip()=="3":
                                                    if calender[0][:2]==date_after_month[:2]:
                                                        e=True
                                                        print(f"> {calender[0].strip()}")
                                                        calender.pop(0)
                                                        print(f"> {calender[0].strip()}")
                                                        calender.pop(0)
                                                        print(f"> {calender[0].strip()}")
                                                        calender.pop(0)
                                                        print(f"> {calender[0].strip()}")
                                                        calender.pop(0)
                                                        if len(calender)>0:
                                                            print(f"> {calender[0].strip()}")
                                                            calender.pop(0)
                                            # this isn't done I can't get it to 
                                            if len(calender)>0: 
                                                if calender[4].strip()=="2":
                                                    num_of_weeks=current_time_cst.tm_yday+n-1
                                                    date=int(calender[0][11:])/7
                                                    date=str(date)[3:]
                                                    date2=num_of_weeks/7
                                                    if date==str(date2)[3:]:
                                                                e=True
                                                                calender.pop(0)
                                                                print(f"> {calender[0].strip()}")
                                                                calender.pop(0)
                                                                print(f"> {calender[0].strip()}")
                                                                calender.pop(0)
                                                                print(f"> {calender[0].strip()}")
                                                                calender.pop(0)
                                                                if len(calender)>0:
                                                                    calender.pop(0)     
                                            if len(calender)>0:                                        
                                                if calender[4].strip()=="1":
                                                    e=True
                                                    print(f"> {calender[0].strip()}")
                                                    calender.pop(0)
                                                    print(f"> {calender[0].strip()}")
                                                    calender.pop(0)
                                                    print(f"> {calender[0].strip()}")
                                                    calender.pop(0)
                                                    print(f"> {calender[0].strip()}")
                                                    calender.pop(0)
                                                    if len(calender)>0:
                                                        print(f"> {calender[0].strip()}")
                                                        calender.pop(0)
                                            if not e:
                                                print("> no enterys")
                                            e=False
                                            next_day=input("> \n> do you want to view the next days events? y/n\n> ")
                                            if next_day=="n":
                                                nextt=False
                                            if next_day=="y":
                                                from datetime import datetime
                                                from dateutil.relativedelta import relativedelta
                                                date_after_month1 = datetime.now()+ relativedelta(days=n)
                                                date_after_month=date_after_month1.strftime("%d\%m\%y")
                                                print(f"> date: {date_after_month}\n> ")
                                                n+=1
                                                nextt=True
                                                while nextt==True:
                                                    nextt=False
                                                    with open("c:\\os\\operating systems\\mxes os\\calender","r") as file:
                                                        calender=file.readlines()
                                                        while len(calender)>0:
                                                            if calender[0].strip()==date_after_month:
                                                                print(f"> {calender[0].strip()}")
                                                                calender.pop(0)
                                                                print(f"> {calender[0].strip()}")
                                                                calender.pop(0)
                                                                print(f"> {calender[0].strip()}")
                                                                calender.pop(0)
                                                                print(f"> {calender[0].strip()}")
                                                                calender.pop(0)
                                                                if len(calender)>0:
                                                                    print(f"> {calender[0].strip()}")
                                                                    calender.pop(0)
                                                            else:
                                                                if len(calender)>0:
                                                                    if calender[4].strip()=="5":
                                                                        calender.pop(0)
                                                                        calender.pop(0)
                                                                        calender.pop(0)
                                                                        calender.pop(0)
                                                                        calender.pop(0)
                                                                        if len(calender)>0:
                                                                            calender.pop(0)
                                                                if len(calender)>0:
                                                                    if calender[4].strip()=="4":
                                                                        if calender[0][:5]==date_after_month[:5]:
                                                                            e=True
                                                                            print(f"> {calender[0].strip()}")
                                                                            calender.pop(0)
                                                                            print(f"> {calender[0].strip()}")
                                                                            calender.pop(0)
                                                                            print(f"> {calender[0].strip()}")
                                                                            calender.pop(0)
                                                                            print(f"> {calender[0].strip()}")
                                                                            calender.pop(0)
                                                                            if len(calender)>0:
                                                                                print(f"> {calender[0].strip()}")
                                                                                calender.pop(0)
                                                                if len(calender)>0:
                                                                    if calender[4].strip()=="3":
                                                                        if calender[0][:2]==date_after_month[:2]:
                                                                            e=True
                                                                            print(f"> {calender[0].strip()}")
                                                                            calender.pop(0)
                                                                            print(f"> {calender[0].strip()}")
                                                                            calender.pop(0)
                                                                            print(f"> {calender[0].strip()}")
                                                                            calender.pop(0)
                                                                            print(f"> {calender[0].strip()}")
                                                                            calender.pop(0)
                                                                            if len(calender)>0:
                                                                                print(f"> {calender[0].strip()}")
                                                                                calender.pop(0)
                                                                # this isn't done I can't get it to 
                                                                if len(calender)>0:
                                                                    if calender[4].strip()=="2":
                                                                        num_of_weeks=current_time_cst.tm_yday+n-1
                                                                        date=int(calender[0][11:])/7
                                                                        date=str(date)[3:]
                                                                        date2=num_of_weeks/7
                                                                        if date==str(date2)[3:]:
                                                                                    e=True
                                                                                    calender.pop(0)
                                                                                    print(f"> {calender[0].strip()}")
                                                                                    calender.pop(0)
                                                                                    print(f"> {calender[0].strip()}")
                                                                                    calender.pop(0)
                                                                                    print(f"> {calender[0].strip()}")
                                                                                    calender.pop(0)
                                                                                    if len(calender)>0:
                                                                                        calender.pop(0)     
                                                                if len(calender)>0:                                        
                                                                    if calender[4].strip()=="1":
                                                                        e=True
                                                                        print(f"> {calender[0].strip()}")
                                                                        calender.pop(0)
                                                                        print(f"> {calender[0].strip()}")
                                                                        calender.pop(0)
                                                                        print(f"> {calender[0].strip()}")
                                                                        calender.pop(0)
                                                                        print(f"> {calender[0].strip()}")
                                                                        calender.pop(0)
                                                                        if len(calender)>0:
                                                                            print(f"> {calender[0].strip()}")
                                                                            calender.pop(0)
                                                                if e==False:
                                                                    print("> no enterys")
                                                                next_day=input("> \n> do you want to view the next days events? y/n\n> ")
                                                                e=False
                                                                if next_day=="y":
                                                                        from datetime import datetime
                                                                        from dateutil.relativedelta import relativedelta
                                                                        date_after_month1 = datetime.now()+ relativedelta(days=n)
                                                                        date_after_month=date_after_month1.strftime("%d\%m\%y")
                                                                        print(f"> date: {date_after_month}\n> ")
                                                                        n+=1
                                                                        nextt=True
                                                                else:
                                                                    nextt=False
        else:
            print("> no enterys in calender")