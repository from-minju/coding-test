# 큰 수의 법칙 - 책 답안예시
n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort()
first = num_list[n-1]
second = num_list[n-2]

count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m-count) * second

print(result)