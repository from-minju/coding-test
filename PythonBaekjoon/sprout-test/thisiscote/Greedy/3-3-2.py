# 숫자 카드 게임 - 책 답안 예시

n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    #현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    #가장 작은 수들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)

'''
로직 : 각 행마다 가장 작은 수를 찾고, 그 수 중에서 가장 큰 수를 찾기.
-> 굳이 이중리스트 만들어서 저장할 필요가 없었음. 바로 비교하면 됨.
-> 내 답안에서는 각 행마다 가장 작은 수 찾은걸 리스트로 저장해서 정렬해서 가장 큰 수를 찾았었는데 그럴 필요없이
max()를 사용하여 이전 값과 비교했을 때 더 큰 수를 남기는 방식으로도 할 수 있음.

'''