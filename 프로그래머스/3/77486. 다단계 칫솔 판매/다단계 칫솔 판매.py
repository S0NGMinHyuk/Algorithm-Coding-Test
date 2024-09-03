def solution(enroll, referral, seller, amount):
    # 자신을 초대한 사람과 자신의 수입을 저장하는 딕셔너리 생성
    corp = {e:[r, 0] for e, r in zip(enroll, referral)}
    
    # 각 칫솔 판매마다 수수료 계산 함수 실행
    for man, income in zip(seller, amount):
        corp = getIncome(corp, man, income*100)
        
    return [corp[man][1] for man in enroll]
    
    
# man에게 income의 90%를 주고, 자신을 초대한 직원에게 10%를 주는 함수
def getIncome(corp, man, income):
    fee = income//10
    corp[man][1] += income - fee
    # 수수료를 줄 수 있는 경우인지 검사
    if fee > 0 and corp[man][0] != "-":
        corp = getIncome(corp, corp[man][0], fee)
    return corp
    