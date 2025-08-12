def solution(commands):
    merged = createMerged()                         # 셀의 병합을 저장하는 배열
    content = [["EMPTY"] * 51 for _ in range(51)]   # 셀의 값을 저장하는 배열
    answer = []
    
    # 셀의 값이 v1이라면 v2로 바꾸는 함수
    def changeContent(v1, v2):
        for i in range(1, 51):
            for j in range(1, 51):
                if content[i][j] == v1:
                    content[i][j] = v2
        return
    
    # UPDATE 명령어를 처리하는 함수
    def update(cmd):
        if len(cmd) == 3:
            value = cmd.pop()
            r, c = map(int, cmd)
            root = merged[r][c]
            content[root[0]][root[1]] = value
        elif len(cmd) == 2:
            v1, v2 = cmd
            changeContent(v1, v2)
        return
    
    # 부모 셀이 root1이라면 root2로 변경하는 함수
    def changeRoot(root1, root2):
        if content[root1[0]][root1[1]] == "EMPTY": # root1 셀 값이 비어있으면 root2 셀 값을 저장
            content[root1[0]][root1[1]] = content[root2[0]][root2[1]]
            
        for i in range(1, 51):
            for j in range(1, 51):
                if merged[i][j] == root2:
                    merged[i][j] = root1
        return
    
    # MERGE 명령어를 처리하는 함수
    def merge(cmd):
        r1, c1, r2, c2 = map(int, cmd)
        root1 = merged[r1][c1]
        root2 = merged[r2][c2]
        changeRoot(root1, root2)
        return
    
    # UNMERGE 명령어를 처리하는 함수
    def unmerge(cmd):
        r, c = map(int, cmd)
        root = merged[r][c]
        value = content[root[0]][root[1]] # 기존 값을 임시로 저장
        for i in range(1, 51):            # 병합된 셀을 모두 초기화
            for j in range(1, 51):
                if merged[i][j] == root:
                    merged[i][j] = (i, j)
                    content[i][j] = "EMPTY"
        content[r][c] = value             # 기존 값을 저장
        return
        
    # PRINT 명령어를 처리하는 함수
    def getValue(cmd):
        r, c = map(int, cmd)
        root = merged[r][c]
        return content[root[0]][root[1]]
    
    
    for cmd in commands:
        cmd = cmd.split()
        if cmd[0] == "UPDATE":
            update(cmd[1:])
        elif cmd[0] == "MERGE":
            merge(cmd[1:])
        elif cmd[0] == "UNMERGE":
            unmerge(cmd[1:])
        elif cmd[0] == "PRINT":
            answer.append(getValue(cmd[1:]))
            
    return answer


# merged 배열을 생성하는 함수
def createMerged():
    merged = []
    for i in range(51):
        temp = []
        for j in range(51):
            temp.append((i, j))
        merged.append(temp)
    return merged
    