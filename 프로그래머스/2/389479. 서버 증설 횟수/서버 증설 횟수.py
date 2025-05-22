from collections import deque

def solution(players, m, k):
    server = deque([])
    count = 0
    
    for time, user in enumerate(players):
        while(len(server) > 0):
            if server[0] <= time:
                server.popleft()
            else:
                break
        
        need = user // m - len(server)
        if need > 0:
            count += need
            for _ in range(need):
                server.append(time+k)
    
    return count