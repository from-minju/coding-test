# 귤고르기 - 딕셔너리와 Key사용

def solution(k, tangerine):
    answer = 0

    # 딕셔너리 생성 (귤사이즈 : 개수)
    dic = {size:0 for size in tangerine} 

    # 개수 세기
    for i in tangerine:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    # 귤의 개수를 기준으로 내림차순 정렬
    dic_sorted = sorted(dic.items(), key=lambda x : x[1], reverse=True)

    total = 0
    for x,y in dic_sorted:
        total += y
        answer += 1
        if total >= k:
            break


    return answer



k = int(input())
tangerine = list(map(int, input().split(', ')))
print(solution(k, tangerine))