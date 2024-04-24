#분해합 -내답1

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

'''
m은 n의 생성자
m의 분해합은 n
n = 256 (245 + 2 + 4 + 5)
m = 245

'''