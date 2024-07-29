def solution(want, number, discount):
    buy = {want[i]:number[i] for i in range(len(want))}
    
    day = 0
    for i in range(10):
        if discount[i] in buy:
            buy[discount[i]] -= 1
    if list(buy.values()) == [0] * len(buy):
        day += 1
    
    for i in range(10, len(discount)):
        if discount[i] in buy:
            buy[discount[i]] -= 1
        if discount[i-10] in buy:
            buy[discount[i-10]] += 1
        if list(buy.values()) == [0] * len(buy):
            day += 1
            
    return day