import math

n = int(input())
k = int(input())

Ckn = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

print(Ckn)
