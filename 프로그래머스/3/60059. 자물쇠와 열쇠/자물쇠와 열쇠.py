def solution(key, lock):
    def expandLock(lock): # lock의 상하좌우로 lock만큼 마진을 채우고 반환하는 함수
        new_lock = [[0] * (len(lock) * 3) for _ in range(len(lock) * 3)]
        for i in range(len(lock), len(lock) * 2):
            for j in range(len(lock), len(lock) * 2):
                new_lock[i][j] = lock[i - len(lock)][j - len(lock)]
        return new_lock
    
    
    def rotateKey(key): # key를 시계방향으로 90도 돌리는 함수
        temp = []
        for col in zip(*key):
            temp.append(list(col[::-1]))
        return temp


    def unlock(lock, key, x, y): # 현재 key로 lock을 풀 수 있는지 여부를 리턴하는 함수
        new_key = [[0] * len(lock) for _ in range(len(lock))]
        for i in range(len(key)):
            for j in range(len(key)):
                new_key[x + i][y + j] = key[i][j]
                
        for i in range(len(lock) // 3, (len(lock) // 3) * 2):
            for j in range(len(lock) // 3, (len(lock) // 3) * 2):
                if lock[i][j] == new_key[i][j]: # 홈이 있거나, 키가 맞지 않는 경우
                    return False
        
        return True
    
    lock = expandLock(lock)         # lock의 길이를 3배로 늘리고, 중앙에 lock을 위치한 배열로 변경
    for _ in range(4):
        key = rotateKey(key)
        for i in range(len(lock) - len(key) + 1):
            for j in range(len(lock) - len(key) + 1):
                if unlock(lock, key, i, j):
                    return True
    return False