#큰 수의 법칙 - 내 답

N, M, K = map(int, input().split())

num_list = list(map(int, input().split()))
num_list.sort(reverse=True)
result = 0

if num_list[0] == num_list[1]:
    result = num_list[0] * M
else:
    result = num_list[0] * (M//K) * K + num_list[1] * (M%K)

print(result)