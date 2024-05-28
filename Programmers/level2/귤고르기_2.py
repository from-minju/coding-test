# 귤고르기

def solution(k, tangerine):
    answer = 0

    dic = {size:0 for size in tangerine}

    for i in tangerine:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    dic_sorted = sorted(dic.items(), key=lambda x : x[1], reverse=True)
    print(dic_sorted)

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