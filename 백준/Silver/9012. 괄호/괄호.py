n = int(input())
for _ in range(n):
    data = input()
    cnt = 0

    for char in data:
        if char == "(":
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                print("NO")
                break
    else:
        print("NO" if cnt else "YES")