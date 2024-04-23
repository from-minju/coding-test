#분해합 - 내답2 (더 빠른)

n = int(input())
ans = []

limit = n - len(str(n))*9
if limit < 0 :
    limit = 1

for m in range(limit, n):
    mlist = list(map(int, str(m)))
    
    if n == m + sum(mlist):
        ans.append(m)

if not ans: #리스트가 비어있는 경우
    print("0")
else:
    ans.sort()
    print(ans[0])

'''

ex) n이 3자리수인 경우
n = m + (각자릿수더한값)
이때, 각 자릿수를 더한 값의 최댓값은 18 = 9+9+9 
(n이 3자리수이므로 m도 최대 3자리수가 될 수있으므로)

n의 최소값은? => n - 18

수식으로 정리하면 : n의 최솟값 = n - (n의자릿수 * 9)

하지만, 이렇게할 경우 n의 최솟값이 음수가 나오는 경우가 있다.
ex) n = 13
n의 최솟값 = 13 - 2*9 = -5
따라서, 음수가 나오면 1부터 n-1까지 탐색한다.

음수가 아닐 경우 위의 최솟값계산식대로 n의최소값 ~ n-1까지 탐색한다.

'''


    
