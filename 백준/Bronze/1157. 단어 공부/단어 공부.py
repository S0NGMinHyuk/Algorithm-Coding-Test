word = input().upper()  # 입력 단어 대문자로 변경

frequency = dict()  # 각 알파벳의 빈도수 저장

for character in word:
    # 각 알파벳마다 frequency 업데이트
    if character not in frequency:
        frequency[character] = 1
    else:
        frequency[character] += 1

mostValue = max(frequency.values()) # 가장 큰 빈도
mostChar = []                       # 가장 많이 나온 알파벳 리스트

for character in frequency.keys():
    if frequency[character] == mostValue:
        mostChar.append(character)

print(mostChar[0] if(len(mostChar) == 1) else "?")