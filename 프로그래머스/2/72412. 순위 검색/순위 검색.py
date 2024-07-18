def solution(info, query):
    # 지원자 정보를 담은 딕셔너리
    dataSet = dict()    
    
    for man in info:
        # 지원자 정보를 리스트로 변환 후 맨뒤 점수를 떼어내기
        man = man.split()
        score = int(man.pop())
        
        # 지원자 정보로 만들 수 있는 모든 key의 value에 점수 추가
        for k in getAllKeys(man, "", 0):
            if k in dataSet:
                dataSet[k].append(score)
            else:
                dataSet[k] = [score]
    
    # 각 키의 지원자 점수를 오름차순으로 정렬
    # query 반복문에서 정렬하면 똑같은 key를 중복해서 정렬하는 경우가 생긴다.
    for k in dataSet.keys():
        dataSet[k].sort()
    
    # 필요한 지원자가 몇명인지 구하는 부분
    answer = []
    for need in query:
        # 문자열을 리스트로 변경 후 점수 떼어내기
        need = need.split() 
        score = int(need.pop())
        
        # need 내용에서 key값을 만들기
        key = ""
        for i in range(0, len(need), 2):
            key += need[i]
        
        # 해당 key값을 만족하는 지원자 중 score 점수 이상인 사람 수를 answer에 추가
        if key in dataSet:
            answer.append(getCandidate(dataSet[key], score))
        # key값을 만족하는 후보가 없는 경우
        else:
            answer.append(0)        
    
    return answer

# lst에서 score 이상의 값이 몇개인지 리턴하는 함수 (이진탐색)
def getCandidate(lst, score):
    left = 0 ; right = len(lst)
    while left < right:
        mid = (left + right) // 2
        if lst[mid] < score:
            left = mid + 1
        else:
            right = mid
    return len(lst) - right
        
# 지원자 정보로 만들 수 있는 모든 key를 담은 배열을 리턴하는 함수
def getAllKeys(man, k, index):
    # base case. 현재 키를 배열에 담아 리턴
    if index == len(man):   
        return [k]
    
    # 지원자의 index 정보를 담은 키와 상관없음("-")을 가진 키 생성
    lst = []
    lst += getAllKeys(man, k+man[index], index+1)
    lst += getAllKeys(man, k+"-", index+1)
    
    return lst