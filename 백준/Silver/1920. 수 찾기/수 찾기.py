# n개의 정수 set 생성. 탐색 효율을 위해 set 자료형으로 저장
n = int(input())
nSet = set(list(map(int, input().split())))

# m개의 정수 리스트 생성.
m = int(input())
mList = list(map(int, input().split()))

# mList의 값이 nSet에 있으면 1, 없으면 0 출력
for num in mList:
    if num in nSet:
        print(1)
    else:
        print(0)