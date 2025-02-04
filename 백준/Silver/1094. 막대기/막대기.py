import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def main():
    target = int(input())
    lst = [64]
    while sum(lst) != target:
        # 가장 짧은 막대기를 반으로 부러뜨린다.
        stick = heappop(lst)
        heappush(lst, stick//2)

        # 전체 길이가 목표 길이보다 짧으면, 부러뜨린 가지를 추가한다.
        if sum(lst) < target:
            heappush(lst, stick//2)
    
    # 막대 개수 리턴
    print(len(lst))


if __name__ == '__main__':
    main()