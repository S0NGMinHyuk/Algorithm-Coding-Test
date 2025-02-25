import sys
input = sys.stdin.readline


def main():
    loop, goal = map(int, input().split())
    coins = sorted([int(input()) for _ in range(loop)])

    lst = [0] * (goal + 1)
    lst[0] = 1

    for c in coins:
        for index in range(c, goal + 1):
            lst[index] += lst[index - c]
    
    print(lst[goal])


if __name__ == '__main__':
    main()