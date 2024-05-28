# 덩치

# 입력
n = int(input())
data = []
for i in range(n):
    data.append(tuple(map(int, input().split())))

# 등수를 구하는 함수
def get_ranking(target):
    ranking = 1 # 등수 초기화

    for cmp in data:
        # if target == cmp: #등수를 구하고있는 사람의 체중,키와 같다면 다음탐색으로 넘어감.
        #     continue

        if cmp[0] > target[0] and cmp[1] > target[1]: # 등수를 구하고 있는 사람보다 더 큰 덩치의 사람이라면
            ranking += 1 # 등수 카운팅
    
    return ranking # 최종 등수 반환

# 출력
for i in data:
    print(get_ranking(i), end = " ")
