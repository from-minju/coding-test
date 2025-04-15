n = int(input())
s, m, l, xl, xxl, xxxl = map(int, input().split())
t, p = map(int, input().split())

ans = 0

# 티셔츠
for size in [s, m, l, xl, xxl, xxxl]:
    if size % t == 0:
        ans += size // t
    else:
        ans += size // t + 1

print(ans)
        
# 펜 
print(n//p, n%p)