N = int(input())

# Если N положительное
if N > 0:
    result = N * (N + 1) // 2
# Если N отрицательное
else:
    result = (N * (N - 1)) // 2 + N

print(result)
