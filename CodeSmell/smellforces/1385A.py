t = int(input())

for i in range(t):
    li = list(map(int, input().split()))
    
    li.sort()
    if li[1] == li[2]:
        print('YES')
        if li[0] == li[1]:
            print(li[0], li[0], li[0])
        else:
            print(li[1], li[0], li[0])
    else:
        print('NO')