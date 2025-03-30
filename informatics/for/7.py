n = int(input())

sum_expression = sum((-1) ** i * 1 / (2 * i + 1) for i in range(n + 1))

result = 4 * sum_expression
print(result)
