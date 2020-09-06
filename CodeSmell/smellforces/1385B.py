t = int(input())

for i in range(t):
    n = int(input())

    di = {}
    for j in range(1, n+1):
        di[j] = 0
    
    li = list(map(int, input().split()))
    result = []
    for k in li:
        if di[k] == 0:
            result.append(str(k))
            di[k] = 1
    print(' '.join(result))