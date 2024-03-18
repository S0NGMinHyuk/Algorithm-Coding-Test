def getNeedToPaint(graph):
    count = 0

    for row in range(8):
        for height in range(8):
            if ((row+height)%2 == 0):
                if graph[row][height] != "B":
                    count += 1
            else:
                if graph[row][height] != "W":
                    count += 1
    
    return min(count, 64-count)


# 메인 코드
n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(input()))


result = 64
for nRow in range(n-7):
    for mColumn in range(m-7):
        temp = []
        for nCnt in range(8):
            arg = []
            for mCnt in range(8):
                arg.append(graph[nRow+nCnt][mColumn+mCnt])
            temp.append(arg)
        result = min(result, getNeedToPaint(temp))


print(result)
