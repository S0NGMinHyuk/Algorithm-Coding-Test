def getGCD(a, b):
    while(b):
        a, b = b, a%b
    return a

a, b = map(int, input().split())
gcd = getGCD(a, b)
print(gcd)
print(a * b // gcd)