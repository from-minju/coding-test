n = int(input())
ans = []

for m in range(n, 0, -1):
    mlist = list(map(int, str(m)))
    
    if n == m + sum(mlist):
        ans.append(m)

ans.sort()
if not ans: #리스트가 비어있는 경우
    print("0")
else:
    print(ans[0])