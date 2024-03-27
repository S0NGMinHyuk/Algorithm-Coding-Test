import sys
input = sys.stdin.readline

n = int(input())

lst = [int(input()) for _ in range(n)]
lst.sort()

for num in lst:
    print(num)