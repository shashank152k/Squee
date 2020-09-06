def findCost(li, c):
    cost = 0
    for i in li:
        if i != c:
            cost += 1
    return cost

def getMinCost(li, c):
    if len(li) == 1:
        if li[0] == c:
            return 0
        else:
            return 1
    
    mid = int(len(li) / 2)

    # print(c, li[:mid], findCost(li[:mid], c))
    # print(c, li[mid:], findCost(li[mid:], c))

    result = min((getMinCost(li[:mid], chr(ord(c)+1)) + findCost(li[mid:], c)) , (getMinCost(li[mid:], chr(ord(c)+1)) + findCost(li[:mid], c)))
    # print(li, result, c)
    return result

t = int(input())

for i in range(t):
    n = int(input())

    li = list(input())

    print(getMinCost(li, 'a'))
