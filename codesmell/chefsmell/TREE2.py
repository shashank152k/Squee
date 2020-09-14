"""
author @shashanknp
created @2020-09-13 20:53:10
"""
T = int(input())

for it in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    A = set(A)
    res = len(A)

    if 0 in A:
        res -= 1
    
    print(res)