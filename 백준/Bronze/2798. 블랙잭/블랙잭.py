n, blackJack = map(int, input().split())
cards = list(map(int, input().split()))

answer = 0

for i in range(n-2):
    if answer == blackJack: break
    for j in range(i+1, n-1):
        if answer == blackJack: break
        for k in range(j+1, n):
            if answer == blackJack: break

            if cards[i] + cards[j] + cards[k] > blackJack:
                continue
            elif cards[i] + cards[j] + cards[k] <= blackJack:
                answer = max(answer, cards[i] + cards[j] + cards[k])

print(answer)