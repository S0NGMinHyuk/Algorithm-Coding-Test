# DP 알고리즘 사용
def solution(n, money):
    dataBase = [0]*(n+1)    # index 원을 거슬러줄 수 있는 경우의 수
    money.sort()            # 코인을 오름차순으로 정렬

    for coin in money:
        for i in range(coin, n+1):
            if i == coin:           
                dataBase[i] += 1
            else:                   
                dataBase[i] += dataBase[i-coin]
    return dataBase[n]