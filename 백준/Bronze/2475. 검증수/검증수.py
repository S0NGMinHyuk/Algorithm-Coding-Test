nums = map(int, input().split())

result = 0
for num in nums:
    result += (num**2) % 10

print(result%10)