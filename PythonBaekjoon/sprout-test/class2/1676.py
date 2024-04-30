# 1676. 팩토리얼 0의 개수

import math

n = int(input())
n = math.factorial(n)
n = list(map(int, str(n))) #n을 리스트로 변환

ans = 0

for i in n[::-1]:
    if i == 0 : ans += 1
    else: break

print(ans)


#같은 방법, 다른 코드
# from math import factorial
# n = int(input())
# cnt = 0
# for x in str(factorial(n))[::-1]:
#     if x != '0':
#         break
#     cnt += 1
# print(cnt)