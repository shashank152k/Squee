"""
author @shashanknp
created @2020-09-08 22:29:19
"""
# [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

# import pandas as pd
# def pprint(li):
#     print(pd.DataFrame(li))

T = int(input())

for it in range(T):
    N = int(input())

    mat = [list(map(int, input().split())) for i in range(N)]
    res = 0

    for x in range(N-1, -1, -1):
        if mat[0][x] == x + 1:
            continue
        else:
            res += 1
            mat = [[mat[j][i] if (i<=x and j<=x) else mat[i][j] for j in range(len(mat))] for i in range(len(mat))]
            # pprint(mat)
    
    print(res)