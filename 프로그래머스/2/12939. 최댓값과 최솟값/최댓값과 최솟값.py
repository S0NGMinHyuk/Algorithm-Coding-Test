def solution(s):
    # 띄어쓰기 기준으로 리스트 생성 + 숫자형으로 변경 + 오름차순 정렬
    s = sorted(list(map(int, s.split())))
    return f"{s[0]} {s[-1]}"    # 최소값과 최대값을 담은 문자열 리턴