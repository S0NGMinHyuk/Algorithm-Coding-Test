dump = int(input())
num = int(input())
answer = 0

while(num > 0):
    answer += num % 10
    num = num // 10

print(answer)