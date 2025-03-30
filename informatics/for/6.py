n = int(input())

sum_series = sum(1 / (i ** 2) for i in range(1, n + 1))

print(sum_series)
