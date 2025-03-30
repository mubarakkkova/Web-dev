def power(a, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(a, -n)
    return a * power(a, n - 1)

a, n = map(int, input().split())
print(power(a, n))
