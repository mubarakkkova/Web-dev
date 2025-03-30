k = int(input())

n = int((2 * k)**0.5)
if n * (n + 1) == 2 * k or n * (n - 1) == 2 * k:
    print("YES")
else:
    print("NO")
