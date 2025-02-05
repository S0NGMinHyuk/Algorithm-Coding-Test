from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def treeDP(node):
    visited[node] = True
    for child in tree[node]:
        if not visited[child]:
            treeDP(child)
            dp[node][0] += min(dp[child])   # node 등대를 켜는 경우, 자식 중 최소 경우를 추가
            dp[node][1] += dp[child][0]     # node 등대를 끄는 경우, 자식은 켠 경우를 추가
    

def solution(n, lighthouse):
    global tree, visited, dp                # 전역변수 선언
    tree = defaultdict(list)                # 트리구조 변수
    visited = [False for _ in range(n+1)]   # 방문여부 검사 배열
    dp = [[1, 0] for _ in range(n+1)]

    # 트리구조 생성
    for a, b in lighthouse:     
        tree[a].append(b)
        tree[b].append(a)
    
    treeDP(1)                   # 1번 노드를 root 노드로 dfs 탐색
    return min(dp[1])           # 1번 노드 배열 중 최소값 리턴