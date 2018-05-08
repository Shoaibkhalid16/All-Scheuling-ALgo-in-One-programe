def FCFS():
    print ("                            this process is for First Come First Serve")
    print('in this process jobs are run according to their arrival time')
    size = int(raw_input("Enter How many Process you want to Enter ??"))

    process = [0] * size
    arrival = [0] * size
    burst = [0] * size
    for i in range(size):
        process[i] = (raw_input("Enter process name"))
        arrival[i] = int(raw_input("Enter Arrival Time for the process"))
        burst[i] = int(raw_input("Enter Burst time for the Process"))
    print(" ")
    print("                             your Enter Pocess Information")
    for i in range(size):
        print(process[i], "     ", arrival[i], "      ", burst[i])

    start = [0] * size
    turn = [0] * size
    wt = [0] * size
    tt = [0] * size
    for j in range(size):
        if j == 0:
            start[j] = arrival[j]
            turn[j] = arrival[j] + burst[j]
        if j >= 1:
            start[j] = turn[j - 1]
            turn[j] = burst[j] + turn[j - 1]

    for k in range(size):
        first1 = min(arrival)
        runn = arrival.index(first1)
        print(process[k], 'arrival time is', arrival[k], ' starts at ', start[k], 'and ends at ', turn[k])

    for m in range(size):
        wt[m] = start[m] - arrival[m]
        tt[m] = turn[m] - arrival[m]
    sum1 = 0
    sum2 = 0
    print("")
    for l in range(size):
        sum1 += wt[l]
        sum2 += tt[l]
        print(process[l], 'waiting time is', wt[l])
        print(process[l], 'turn time is', tt[l])
    awt = sum1 / size
    att = sum2 / size
    print("")
    print('average waiting time is: ', awt)
    print('average turn around time is: ', att)


def SJF():
    print("                           this process is for SHortest Job first")
    print('in this process jobs are run according to their shortest burst time')
    size = int(raw_input("Enter How many Process you want to Enter ??"))

    process = [0] * size
    arrival = [0] * size
    burst = [0] * size
    for i in range(size):
        process[i] = (raw_input("Enter process name"))
        arrival[i] = int(raw_input("Enter Arrival Time for the process"))
        burst[i] = int(raw_input("Enter Burst time for the Process"))
    print(" ")
    print("                             your Enter Pocess Information")
    for i in range(size):
        print(process[i], "     ", arrival[i], "      ", burst[i])
    start = [0] * size
    turn = [0] * size
    wt = [0] * size
    tt = [0] * size

    for i in range(0,size):
        min1=i
        for j in range(i+1,(size)):
            if burst[min1]>burst[j]:
                temp1=burst[j]
                burst[j]=burst[min1]
                burst[min1]=temp1

                temp2=arrival[j]
                arrival[j]=arrival[min1]
                arrival[min1]=temp2

                temp3 = process[j]
                process[j] = process[min1]
                process[min1] = temp3

    for j in range(size):
        if j == 0:
            start[j] = arrival[j]
            turn[j] = arrival[j] + burst[j]
        if j >= 1:
            start[j] = turn[j - 1]
            turn[j] = burst[j] + turn[j - 1]

    for j in range(size):
        first1=min(burst)
        runn=burst.index(first1)
        print(process[j], 'arrival time is', arrival[j], ' starts at ', start[j], 'and ends at ', turn[j])

    for m in range(size):
        wt[m] = start[m] - arrival[m]
        tt[m] = turn[m] - arrival[m]
    sum1 = 0
    sum2 = 0
    print("")
    for l in range(size):
        sum1 += wt[l]
        sum2 += tt[l]
        print(process[l], 'waiting time is', wt[l])
        print(process[l], 'turn time is', tt[l])
    awt = sum1 / size
    att = sum2 / size
    print("")
    print('average waiting time is: ', awt)
    print('average turn around time is: ', att)

def RR():
    print("                                    This Is Round Robin Process")
    size = int(raw_input("Enter How many Process you want to Enter ??"))

    process = [0] * size
    arrival = [0] * size
    burst = [0] * size
    totaltime=0
    for i in range(size):
        process[i] = (raw_input("Enter process name"))
        arrival[i] = int(raw_input("Enter Arrival Time for the process"))
        burst[i] = int(raw_input("Enter Burst time for the Process"))
        totaltime+=burst[i]
    qt=int(raw_input("ENter quantum time"))
    print(" ")
    print("                             your Enter Pocess Information")
    for i in range(size):
        print(process[i], "     ", arrival[i], "      ", burst[i])
    print('Quantum time is: ',qt)
    turn = [0] * size
    wt = [0] * size
    rt = [0] * size
    waitingtime=[0]*size
    turntime=[0]*size
    for i in range(size):
        rt[i]=burst[i]
    time=0
    while True:
        done=True
        for i in range(size):
            if rt[i]>0:
                done=False
                if rt[i]>qt:
                    time+=qt
                    rt[i]-=qt
                else:
                    time=time+rt[i]
                    wt[i]=time-burst[i]
                    rt[i]=0

        if done==True:
            break

    for i in range (size):
        turn[i]=burst[i]+wt[i]

    for j in range(size):
        turntime[j]=turn[j]-arrival[j]
        waitingtime[j]=turn[j]-arrival[j]-burst[j]

    sum1=0
    sum2=0

    for k in range(size):
        sum1+=waitingtime[k]
        sum2+=turntime[k]
    awt=sum1/size
    atat=sum2/size

    for j in range(size):
        first1 = min(burst)
        runn = burst.index(first1)
        print(process[j], 'arrival time is', arrival[j], 'and ends at ', turn[j])

    print('average waiting time is',awt)
    print('average turn around time is',atat)

def MLFQ():
    def Queue(id):
        if id == 0 or id == 1 or id == 2 or id == 3:
            return 1
        else:
            return 2

    print("                                    This Is MultiLevel feedback Queue Process")
    size = int(raw_input("Enter How many Process you want to Enter ??"))

    process = [0] * size
    arrival = [0] * size
    burst = [0] * size
    wt=[0]*size
    turn =[0]*size
    tat=[0]*size
    start=[0]*size
    q = [0] * size
    ready = [0] * size
    priority = [0] * size
    for i in range(size):
        process[i] = (raw_input("Enter process name"))
        arrival[i] = int(raw_input("Enter Arrival Time for the process"))
        burst[i] = int(raw_input("Enter Burst time for the Process"))
        priority[i] = int(raw_input('Enter Priority of the process'))
        temp_process = priority[i]
        q[i] = Queue(temp_process)
        ready[i] = 0

    print(" ")
    print("                             your Enter Pocess Information")
    for i in range(size):
        print(process[i], "     ", arrival[i], "      ", burst[i], "        ", priority[i])

    time = burst[0]
    for y in range(size):
        for count in range(y, size):
            if arrival[count] < time:
                ready[count] = 1

        for count in range(y, size - 1):
            for j in range(count + 1, size):
                if ready[count] == 1 and ready[j] == 1:
                    if q[count] == 2 and q[j] == 1:
                        temp1 = burst[j]
                        burst[j] = burst[count]
                        burst[count] = temp1

                        temp2 = arrival[j]
                        arrival[j] = arrival[count]
                        arrival[count] = temp2

                        temp3 = process[j]
                        process[j] = process[count]
                        process[count] = temp3

                        temp4 = priority[j]
                        priority[j] = priority[count]
                        priority[count] = temp4

                        temp5 = q[j]
                        q[j] = q[count]
                        q[count] = temp5

                        temp6 = ready[j]
                        ready[j] = ready[count]
                        ready[count] = temp6
        for count in range(y, size - 1):
            for j in range(count + 1, size):
                if ready[count] == 1 and ready[j] == 1:
                    if q[count] == 1 and q[j] == 1:
                        if burst[count] > burst[j]:
                            temp1 = burst[j]
                            burst[j] = burst[count]
                            burst[count] = temp1

                            temp2 = arrival[j]
                            arrival[j] = arrival[count]
                            arrival[count] = temp2

                            temp3 = process[j]
                            process[j] = process[count]
                            process[count] = temp3

                            temp4 = priority[j]
                            priority[j] = priority[count]
                            priority[count] = temp4

                            temp5 = q[j]
                            q[j] = q[count]
                            q[count] = temp5

                            temp6 = ready[j]
                            ready[j] = ready[count]
                            ready[count] = temp6
                        else:
                            break

        for count in range(y, size):
            if ready[count] == 1:
                ready[count] = 0
    for j in range(size):
        if j == 0:
            start[j] = arrival[j]
            turn[j] = arrival[j] + burst[j]
        if j >= 1:
            start[j] = turn[j - 1]
            turn[j] = burst[j] + turn[j - 1]

    wtavg = tatavg = 0
    for i in range(size):
        wt[i] = turn[i] - arrival[i] - burst[i]
        tat[i] = turn[i] - arrival[i]
        wtavg = wtavg + wt[i]
        tatavg = tatavg + tat[i]
    wtavg /= size
    tatavg /= size
    print('process    start time    burst time    turnaround time')
    for i in range(size):
        print(process[i], start[i], burst[i], turn[i])

    print('Average Waiting time is: ', wtavg)
    print('Average Turn Around time is: ', tatavg)

def MLQ():
    print("                                    This Is MultiLevel Queue Process")
    size = int(raw_input("Enter How many Process you want to Enter ??"))
    process = [0] * size
    arrival = [0] * size
    burst = [0] * size
    start=[0]*size
    turn=[0]*size
    wt=[0]*size
    tat=[0]*size
    systemuser=[0]*size
    for i in range(size):
        process[i] = (raw_input("Enter process name"))
        arrival[i] = int(raw_input("Enter Arrival Time for the process"))
        burst[i] = int(raw_input("Enter Burst time for the Process"))
        systemuser[i]=int(raw_input('Enter 0 for system process and 1 for interactive process and 2 for user process'))
    print(" ")
    print("                             your Enter Pocess Information")
    for i in range(size):
        print(process[i], "     ", arrival[i], "      ", burst[i],'        ',systemuser[i])
    for i in range(size):
        for k in range(i + 1, size):
            if systemuser[i] > systemuser[k]:
                temp1 = burst[k]
                burst[k] = burst[i]
                burst[i] = temp1

                temp2 = arrival[k]
                arrival[k] = arrival[i]
                arrival[i] = temp2

                temp3 = process[k]
                process[k] = process[i]
                process[i] = temp3

                temp4 = systemuser[k]
                systemuser[k] = systemuser[i]
                systemuser[i] = temp4

    for j in range(size):
        if j == 0:
            start[j] = arrival[j]
            turn[j] = arrival[j] + burst[j]
        if j >= 1:
            start[j] = turn[j - 1]
            turn[j] = burst[j] + turn[j - 1]

    wtavg=tatavg=0
    for i in range (size):
        wt[i] = turn[i]-arrival[i]-burst[i]
        tat[i] = turn[i]-arrival[i]
        wtavg = wtavg + wt[i]
        tatavg = tatavg + tat[i]
    wtavg/=size
    tatavg/=size
    print('process    system/interactive/user    start time    burst time    turnaround time     waiting time')
    for i in range(size):
        print(process[i], systemuser[i], start[i], burst[i], turn[i], wt[i])

    print('Average Waiting time is: ',wtavg)
    print('Average Turn Around time is: ', tatavg)



def VRR():
    print("                                    This Is virtual Round Robin Process")
    size = int(raw_input("Enter How many Process you want to Enter ??"))

    process = [0] * size
    arrival = [0] * size
    burst = [0] * size
    totaltime = 0
    for i in range(size):
        process[i] = (raw_input("Enter process name"))
        arrival[i] = int(raw_input("Enter Arrival Time for the process"))
        burst[i] = int(raw_input("Enter Burst time for the Process"))
        totaltime += burst[i]
    qt = int(raw_input("ENter quantum time"))
    io=int(raw_input("Enter inout output time"))
    print(" ")
    print("                             your Enter Pocess Information")
    for i in range(size):
        print(process[i], "     ", arrival[i], "      ", burst[i])
    print('Quantum time is: ', qt)
    print('Input Output Time is',io)
    turn = [0] * size
    wt = [0] * size
    rt = [0] * size
    waitingtime=[0]*size
    turntime=[0]*size
    for i in range(size):
        rt[i]=burst[i]
    time=0
    while True:
        done=True
        for i in range(size):
            if rt[i]>0:
                done=False
                if rt[i]>qt:
                    time+=qt
                    rt[i]-=qt
                else:
                    time=time+rt[i]
                    wt[i]=time-burst[i]
                    rt[i]=0
            if wt[i]==io:
                wt[i]+=io
        if done==True:
            break

    for i in range (size):
        turn[i]=burst[i]+wt[i]

    for j in range(size):
        turntime[j]=turn[j]-arrival[j]
        waitingtime[j]=turn[j]-arrival[j]-burst[j]

    sum1=0
    sum2=0

    for k in range(size):
        sum1+=waitingtime[k]
        sum2+=turntime[k]
    awt=sum1/size
    atat=sum2/size

    for j in range(size):
        first1 = min(burst)
        runn = burst.index(first1)
        print(process[j], 'arrival time is', arrival[j], 'and ends at ', turn[j])

    print('average waiting time is',awt)
    print('average turn around time is',atat)


print('1) First come first serve')
print('2) shortest job first')
print('3) Round Robin')
print('4) Virtual Robin Robin')
print('5) MultiLevel Queue')
print('6) MultiLevel FeedBack Queue')
choice=int(raw_input('enter your choice: '))

if(choice==1):
    FCFS()
elif(choice==2):
    SJF()
elif(choice==3):
    RR()
elif(choice==4):
    VRR()
elif(choice==5):
    MLQ()
elif(choice==6):
    MLFQ()
else:
    print("invalid choice")
