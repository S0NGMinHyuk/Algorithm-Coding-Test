import sys
input = sys.stdin.readline
INF = float("Inf")

def main():
    loop, goal = map(int, input().split())
    coins = sorted([int(input()) for _ in range(loop)])
    
    # DP용 배열 생성
    lst = [INF] * (goal+1)
    lst[0] = 0

    # 목표 금액까지 반복
    for i in range(1, len(lst)):
        for coin in coins:
            if coin > i: break
            elif lst[i-coin] + 1 < lst[i]:  # 현재 코인을 사용하는게 더 유리한 경우
                lst[i] = lst[i-coin] + 1
    
    # 사용한 동전의 개수 리턴, 불가능하면 -1 리턴
    print(lst[-1] if lst[-1] != INF else -1)


if __name__ == '__main__':
    main()