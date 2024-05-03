#1920. 수 찾기

n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

set_a = set(m_list) & set(n_list)

for i in m_list:
    if i in set_a: print(1)
    else: print(0)


# n = int(input())
# n_list = list(map(int, input().split()))

# m = int(input())
# m_list = list(map(int, input().split()))

# for i in m_list:
#     if i in n_list: print(1)
#     else: print(0)



'''
N
N개의 정수
M
M개의 수 -> 이 수들이 A안에 존재하는지

M개의 줄에 답 출력 1/0
'''