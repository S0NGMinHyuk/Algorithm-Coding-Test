import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
dict = {}
for card in cards:
    if card not in dict:
        dict[card] = 1
    else:
        dict[card] += 1

n = int(input())
answer = list(map(int, input().split()))
for i in range(len(answer)):
    if answer[i] not in dict:
        answer[i] = "0"
    else:
        answer[i] = str(dict[answer[i]])

print(" ".join(answer))