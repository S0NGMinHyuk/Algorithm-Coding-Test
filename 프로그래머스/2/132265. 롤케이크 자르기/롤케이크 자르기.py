def solution(topping):
    # 모든 토핑을 가져가는 경우 A
    a = dict()
    for t in topping:
        a[t] = a[t]+1 if t in a else 1
    
    # B가 앞에서부터 토핑을 가져가고, B가 가져간만큼 A의 토핑을 줄인다
    b = dict()
    cnt = 0
    for t in topping:
        b[t] = b[t]+1 if t in b else 1
        a[t] -= 1
        if a[t] == 0: del a[t]          # A에 토핑이 없다면 제거
        if len(a) == len(b): cnt += 1   # A와 B의 토핑 개수가 같으면 cnt 1 증가
    
    return cnt