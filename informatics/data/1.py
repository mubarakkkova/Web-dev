def IsDigit(c):
    return c.isdigit()

c = input().strip()
if IsDigit(c):
    print("yes")
else:
    print("no")
