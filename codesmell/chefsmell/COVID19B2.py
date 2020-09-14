"""
author @shashanknp
created @2020-09-12 19:23:57
"""
import pandas as pd
def pprint(li):
    print(pd.DataFrame(li))

def findInfected(i, j, a, b, time):
    # print(i, j)
    if b >= a:
        return 0
    else:
        t = ((j - i) / (a - b))
        if t.is_integer():
            time[i][int(t)+1].append(j)
            time[j][int(t)+1].append(i)
            return int(t)+1
        return 0

T = int(input())

for it in range(T):
    N = int(input())
    V = list(map(int, input().split()))
    print(V)
    athletes = [[None]*N for i in range(N)]
    time = [[[] for i in range(22)] for i in range(N)]
    
    for i in range(N):
        for j in range(i, N):
            if i == j:
                athletes[i][j] = 1
                continue
            athletes[i][j] = findInfected(i, j, V[i], V[j], time)
            athletes[j][i] = athletes[i][j]
    
    pprint(athletes)
    pprint(time)

    infected = []
    for i in range(N):
        infectedi = 1
        for j in range(N):
            if i == j:
                continue
            else:
                infectedi += 1
                for k in time[j][athletes[i][j]:]:
                    for l in k:
                        if not athletes[i][l]:
                            infectedi += 1
        infected.append(infectedi)
    
    # print(infected)
    print(min(infected), max(infected))



# """
# author @shashanknp
# created @2020-09-12 19:23:57
# """
# import pandas as pd
# def pprint(li):
#     print(pd.DataFrame(li))

# def bitwiseOR(li):
#     res = li[0]
#     for i in range(1, len(li)):
#         for j in range(len(li[i])):
#             res = [res[j] | li[i][j] for j in range(len(res))]
    
#     return res

# def compareInfected(i, j, t):
#     li = []
#     liRecur = None
#     for x in range(len(dp[j])):
#         if dp[j][x] >= t:
#             li.append(1)
#             liRecur = compareInfected(j, x, dp[j][x])
#         else:
#             li.append(0)
    
#     return [li] + liRecur

# def findInfected(i, j, a, b):
#     if b >= a:
#         return 0
#     else:
#         t = ((j - i) / (a - b))
#         if t.is_integer():
#             return int(t)+1
#         return 0

# T = int(input())

# for it in range(T):
#     N = int(input())
#     V = list(map(int, input().split()))

#     dp = [[None]*N for i in range(N)]
    
#     for i in range(N):
#         for j in range(i, N):
#             if i == j:
#                 dp[i][j] = 1
#                 continue
#             dp[i][j] = findInfected(i, j, V[i], V[j])
#             dp[j][i] = dp[i][j]
    
#     pprint(dp)
    
#     infected = []
#     for i in range(N):
#         li = []
#         for j in dp[i]:
#             if j:
#                 li.append(1)
#             else:
#                 li.append(0)

#         strLi = [li]
#         for j in range(N):
#             if dp[i][j]:
#                 strLi += compareInfected(i, j, dp[i][j])

#         infected.append(bitwiseOR(strLi).count(1))
#     print(infected)
#     print(min(infected), max(infected))