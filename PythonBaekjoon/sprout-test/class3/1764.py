# 듣보잡

n, m = map(int, input().split())

h = set(input() for _ in range(n))
s = set(input() for _ in range(m))

hs =  list(h & s)
hs.sort()

print(len(hs))
for i in hs:
    print(i)

