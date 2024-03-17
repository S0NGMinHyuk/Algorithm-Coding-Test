word = input()
lst = [-1] * 26

for i in range(len(word)):
    if(lst[ord(word[i]) - ord('a')] == -1):
        lst[ord(word[i]) - ord('a')] = i


print(" ".join(map(str, lst)))