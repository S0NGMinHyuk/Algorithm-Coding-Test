while(1):
    # 입력 숫자
    number = input()

    # 반복문 종료조건. 입력 숫자가 0일 경우 종료
    if number == "0":
        break
    
    # number 길이를 반으로 나눈 후 반올림한 값 저장
    halfLen = len(number)//2 if len(number)%2 == 0 else len(number)//2 +1
    
    # 앞과 뒤에서 동시에 읽으며 값이 다르면 no 리턴, 펠린드롬 조건을 만족하면 yes 리턴
    for i in range(halfLen):
        if number[i] != number[-(i+1)]:
            print("no")
            break
    else:
        print("yes")