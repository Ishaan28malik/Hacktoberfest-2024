import clinkedlist as c

proc = c.CLinkedList()

quantum = 2
n = 3
rem_bt = [4,6,8]

while(1):
    done = True

    for i in range(n):
        if rem_bt[i] > 0:
            done = False
            if i == 0:
                print("Currently Processing P1 with remaining time: ", rem_bt[i])
                proc.AtBeginning('P1')
                if proc.listcount() > 3:
                    proc.removeEnd()
                proc.listprint()
            if i == 1:
                print("Currently Processing P2 with remaining time: ", rem_bt[i])
                proc.AtBeginning('P2')
                if proc.listcount() > 3:
                    proc.removeEnd()
                proc.listprint()
            if i == 2:
                print("Currently Processing P3 with remaining time: ", rem_bt[i])
                proc.AtBeginning('P3')
                if proc.listcount() > 3:
                    proc.removeEnd()
                proc.listprint()

            if rem_bt[i] > quantum:
                rem_bt[i] -= quantum
            else:
                rem_bt[i] = 0
                
    if done ==  True:
        break
