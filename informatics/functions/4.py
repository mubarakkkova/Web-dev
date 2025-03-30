def Election(x, y, z):
    votes = [x, y, z]
    count_true = votes.count(True)
    count_false = votes.count(False)
    return count_true > count_false

x, y, z = map(int, input().split())
print(int(Election(x, y, z)))
