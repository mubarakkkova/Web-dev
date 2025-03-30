a = float(input())
n = int(input())

sum_gp = sum(a ** i for i in range(n + 1))

print(sum_gp)
