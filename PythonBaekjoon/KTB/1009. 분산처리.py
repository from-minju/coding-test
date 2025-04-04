t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    patternNum = int(str(a)[-1])

    if patternNum==0:
        print(10)
        continue

    pattern = [[1], [4, 8, 6, 2], [9, 7, 1, 3], [6, 4], [5], [6], [9, 3, 1, 7], [4, 2, 6, 8], [1, 9]]

    print(pattern[patternNum-1][(b-1) % len(pattern[patternNum-1]) - 1])

# 1 : 1
# 2 : 4 8 6 2 / 4 8 6 2
# 3 : 9 7 1 3 / 9 7 1 3 ...
# 4 : 6 4 6 4 ...
# 5 : 5 5 ...
# 6 : 6 6 6 6 ...
# 7 : 9 3 1 7 / 9 ...
# 8 : 4 2 6 8 / 4 2 ...
# 9 : 1 9 1 9 ...


def my_ans1_timeout():
    t = int(input())

    for i in range(t):
        a, b = map(int, input().split())
        target = a ** b

        if target==10:
            print(10)
            break

        target = str(target)
        print(target[-1])