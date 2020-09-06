t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int, input().split()))
    
    j = n - 1
    while j > 0 and li[j] <= li[j-1]:
        j -= 1
    while j > 0 and li[j] >= li[j-1]:
        j -= 1
    print(j)
