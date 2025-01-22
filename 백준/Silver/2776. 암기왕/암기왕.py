import sys

def getNote1():
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    return {num : 1 for num in nums}


def printAnswer(note1:dict):
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    for num in nums:
        print(int(num in note1))


def main():
    n = int(sys.stdin.readline())
    for _ in range(n):
        note1 = getNote1()
        printAnswer(note1)

main()
