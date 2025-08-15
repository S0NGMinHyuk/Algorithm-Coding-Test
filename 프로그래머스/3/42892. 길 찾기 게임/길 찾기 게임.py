import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    def dfs(nodeinfo):
        root_index = 0
        root_height = -1
        root_number = 0
        if len(nodeinfo) > 0:
            for i, (index, height, number) in enumerate(nodeinfo):
                if root_height < height:    # 루트노드 찾기
                    root_height = height
                    root_index = i
                    root_number = number
            answer[0].append(root_number)   # 전위 순회
            dfs(nodeinfo[:root_index])      # 왼쪽 서브트리 재귀
            dfs(nodeinfo[root_index+1:])    # 오른쪽 서브트리 재귀
            answer[1].append(root_number)   # 후위 순회
        return
            
        
    answer = [[], []]
    nodeinfo = list(sorted([(x, y, i+1) for i, (x, y) in enumerate(nodeinfo)]))
    dfs(nodeinfo)
    return answer