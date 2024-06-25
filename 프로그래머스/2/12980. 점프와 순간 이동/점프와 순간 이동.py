def solution(n):
    usage = 0   # 건전지 사용량
    while n > 0:
        n, mod = divmod(n, 2)
        if mod > 0:
            usage += 1  # 점프 후 이동이 필요한 경우 건전지 1 사용
    return usage