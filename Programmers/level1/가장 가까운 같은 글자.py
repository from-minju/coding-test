def solution(s):
    answer = []
    dic = {}
    
    for idx, i in enumerate(s):
        if i in dic:
            answer.append(idx - dic[i])
        else:
            answer.append(-1)
        dic[i] = idx
    
    return answer