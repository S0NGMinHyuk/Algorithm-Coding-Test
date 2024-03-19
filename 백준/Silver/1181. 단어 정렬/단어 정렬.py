n = int(input())

# 단어들을 set 자료형에 추가. 중복값 제거
words = set()
for _ in range(n):
    words.add(input())

# 단어 사전순으로 정렬 후 길이 순으로 정렬
words = sorted(words)
words = sorted(list(words), key = lambda x : len(x))

# 제출
for word in words:
    print(word)