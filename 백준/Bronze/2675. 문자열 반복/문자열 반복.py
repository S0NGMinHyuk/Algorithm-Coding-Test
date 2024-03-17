repeat = int(input())
for _ in range(repeat):
    multi, sentence = input().split()
    multi = int(multi)

    temp = ""
    for char in sentence:
        temp += char * multi
    print(temp)