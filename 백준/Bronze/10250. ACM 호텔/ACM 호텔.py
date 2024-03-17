def getFront(floor, customer):
    a, b = divmod(customer, floor)

    if b == 0:
        return floor
    return b


def getRear(floor, customer):
    a, b = divmod(customer, floor)

    if b == 0:
        return a
    else:
        return a+1
    
repeat = int(input())

for _ in range(repeat):
    floor, room, customer = map(int, input().split())

    front = getFront(floor, customer)
    rear = getRear(floor, customer)

    if rear < 10:
        print(str(front)+"0"+str(rear))
    else:
        print(str(front)+str(rear))

