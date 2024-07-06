import time
ops=[]
es=[]
times=[]
def run(run_num):
    time4=time.time()
    run_num2=run_num
    while run_num>0:
        e=0
        time1=time.time()
        time22=time1+1
        time3=time1
        op=11
        while time1<time22:
            time1=time.time()
            e+=1
            op+=9
        run_num-=1
        print(f"GigaFlops: {op/100000} run time: {round(time1-time3,2)}")
        ops.append(op)
        times.append(round(time1-time3,2))
    while len(times)>1:
        times[0]+=times[1]
        times.pop(1)
    while len(ops)>1:
        ops[0]+=ops[1]
        ops.pop(1)
    ops2=ops[0]/run_num2
    times2=times[0]/run_num2
    time5=time.time()
    print(f"avg: GigaFlops: {ops2/100000} run time: {times2} tot run time: {time5-time4/60}")
run(int(input("> input number of runs\n> ")))