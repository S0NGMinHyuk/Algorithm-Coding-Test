def solution(order):
    answer = 4500 * len(order)
    for menu in order:
        if menu[0] == 'c' or menu[3] == 'c':
            answer += 500
    return answer