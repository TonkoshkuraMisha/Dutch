a, b = map(int, input().split())
n = 0
while a != b:
    n += 1
    if a > b:
        a = a - b
    else:
        b = b - a

print(a + b, n)
