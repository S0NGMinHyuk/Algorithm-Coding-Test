import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())
arr = map(int, input().split())
results = sorted(list(permutations(arr, M)))
for r in results:
    for num in r:
        print(f"{num} ", end="")
    print("")