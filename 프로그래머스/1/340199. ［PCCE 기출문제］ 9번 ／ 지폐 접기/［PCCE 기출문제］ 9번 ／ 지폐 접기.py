def solution(wallet, bill):
    answer = 0
    wallet = setArray(wallet)
    bill = setArray(bill)
    
    while not (bill[0] <= wallet[0] and bill[1] <= wallet[1]):
        bill = fold(bill)
        answer += 1
        
    return answer


def setArray(arr):
    if arr[0] < arr[1]:
        return arr[::-1]
    return arr


def fold(bill):
    bill[0] = bill[0] // 2
    return setArray(bill)