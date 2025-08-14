from copy import deepcopy

def solution(beginning, target):
    def createTable():
        table = []
        for i in range(len(target)):
            temp = []
            for j in range(len(target[0])):
                temp.append(beginning[i][j] == target[i][j])
            table.append(temp)
        return table
    
    answer = -1
    save = createTable()
    
    for do in [True, False]:
        # 행 뒤집고 열 뒤집기
        table = deepcopy(save) # 2차원 배열부터는 deepcopy 사용
        cnt = 0
        for i in range(len(table)):
            if table[i][0] == do:
                flip(table, True, i)
                cnt += 1
        for i in range(len(table[0])):
            if table[0][i] == False:
                flip(table, False, i)
                cnt += 1
        if isClear(table):
            if answer == -1 or cnt < answer:
                answer = cnt
        
        # 열 뒤집고 행 뒤집기
        table = deepcopy(save) # 2차원 배열부터는 deepcopy 사용
        cnt = 0
        for i in range(len(table[0])):
            if table[0][i] == do:
                flip(table, False, i)
                cnt += 1
        for i in range(len(table)):
            if table[i][0] == False:
                flip(table, True, i)
                cnt += 1
        if isClear(table):
            if answer == -1 or cnt < answer:
                answer = cnt
        
    return answer 


def flip(table, direct, index) -> None:
    if direct:  # 행을 뒤집는 경우
        for i in range(len(table[0])):
            table[index][i] = not table[index][i]
    else:       # 열을 뒤집는 경우
        for i in range(len(table)):
            table[i][index] = not table[i][index]
    return

            
def isClear(table) -> bool: # table이 모두 True인지 여부를 리턴
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == False:
                return False
    return True