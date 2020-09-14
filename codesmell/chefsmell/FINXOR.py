"""
author @shashanknp
created @2020-09-13 19:50:49
"""
A = [0]*21
A[0] = 1
for i in range(1, 21):
    A[i] = A[i-1] * 2

T = int(input())

for it in range(T):
    N = int(input())

    print(1, A[20])
    s = int(input()) - (N * A[20])

    res = 0
    if s % 2 != 0:
        res = 1
    
    for i in range(1, 20):
        tempS = (N * A[i]) + s
        print(1, A[i])
        inpS = int(input())
        
        if ((tempS - inpS) / (2 * A[i])) % 2 != 0:
            res += A[i]
    
    print(2, res)
    output = int(input())