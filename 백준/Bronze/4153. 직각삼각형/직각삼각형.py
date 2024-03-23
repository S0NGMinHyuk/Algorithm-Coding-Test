while(1):
    numbers = list(map(int, input().split()))

    if sum(numbers) == 0:
        break
    else:
        numbers = sorted(numbers)
    
    if numbers[2] ** 2 == numbers[0] ** 2 + numbers[1] ** 2:
        print("right")
    else:
        print("wrong")