"""
author @shashanknp
created @2020-09-13 13:11:52
"""
import math

T = int(input())

for it in range(T):
    N = int(input())

    sumTillN = int((N*(N+1)) / 2)
    # print(N, sumTillN, end=' ')
    if sumTillN % 2 == 1:
        print(0)
    else:
        temp = sumTillN / 2
        k = (math.sqrt(8*temp + 1) / 2) - 0.5
        kTemp = math.floor(k)
        res = 0
        if k.is_integer():
            res = int(((kTemp - 1) * kTemp) / 2) + int(((N-kTemp - 1) * (N-kTemp)) / 2)
        
        res += N - kTemp

        print(int(res))