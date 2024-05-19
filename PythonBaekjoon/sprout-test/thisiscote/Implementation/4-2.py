# 시각 - 내 답

n = int(input())
cnt = 0

for h in range(n+1):
    if '3' in str(h):
        cnt += 3600
    else:
        for m in range(60):
            if '3' in str(m):
                cnt += 60
            else:
                for s in range(60):
                    if '3' in str(s):
                        cnt += 1

print(cnt)