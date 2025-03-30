import math

n, m = map(int, input().split())

max_rabbits_per_cell = math.ceil(m / n)
print(max_rabbits_per_cell)
