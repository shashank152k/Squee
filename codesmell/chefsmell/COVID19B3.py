"""
author @shashanknp
created @2020-09-13 01:30:51
"""
def findInfected(i, time, V, current, pos):
    if pos[i] == 1:
        return
    pos[i] = 1
    for j in range(len(V)):
        if time[i][j] > current:
            findInfected(j, time, V, time[i][j], pos)
    
    return pos

T = int(input())

for it in range(T):
    N = int(input())
    V = list(map(int, input().split()))

    time = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            if i == j:
                time[i][j] = 0
            else:
                if V[i] == V[j]:
                    time[i][j], time[j][i] = 0, 0
                else:
                    t = (i-j)/(V[j]-V[i])
                    if t > 0:
                        time[i][j], time[j][i] = t, t
                    else:
                        time[i][j], time[j][i] = 0, 0
    
    infected = []
    for i in range(N):
        infected.append(findInfected(i, time, V, 0, [0 for i in range(N)]).count(1))
    
    print(min(infected), max(infected))
