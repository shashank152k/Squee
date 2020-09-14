"""
author @shashanknp
created @2020-09-09 20:23:49
"""
def findInfected(i, infectedPos, called, V, time):
    if called == infectedPos:
        return
    
    called[i] = 1
    
    for j in range(len(V)):
        if i == j or infectedPos[j]:
            continue
        pos1 = time * V[i] + i
        pos2 = time * V[j] + j
        # if pos1 < pos2 and V[j] >= V[i]:
        #     continue
        # print(pos1, pos2)
        # a = V[i]
        # b = V[j]
        
        # if a - b != 0:
        #     t = ((pos2 - pos1) / (a - b))
        #     if t > 0 and t.is_integer():
                # infectedPos[j] = 1
                # if not called[j]:
                #     called[j] = 1
                #     findInfected(j, infectedPos, called, V, int(t+1))
        if pos2 < pos1 and V[j] > V[i]:
            infectedPos[j] = 1
            if not called[j]:
                called[j] = 1
                findInfected(j, infectedPos, called, V, ((pos1-pos2)/(V[j]-V[i])))
        elif pos1 < pos2 and V[j] < V[i]:
            infectedPos[j] = 1
            if not called[j]:
                called[j] = 1
                findInfected(j, infectedPos, called, V, ((pos2-pos1)/(V[i]-V[j])))


T = int(input())

for it in range(T):
    N = int(input())
    V = list(map(int, input().split()))
    
    infected = []
    # print('\n', V)
    for i in range(N):
        infecti = 1
        infectedPos = [0]*N
        infectedPos[i] = 1
        called = [0]*N
        current = [i for i in range(N)]

        # print(infectedPos, N)
        # print('Parent Calling with', i, infectedPos)
        findInfected(i, infectedPos, called, V, 0)
        infected.append(infectedPos.count(1))
        # print(infectedPos.count(1))

    print(min(infected), max(infected))
