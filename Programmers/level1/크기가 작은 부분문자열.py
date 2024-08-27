def solution(t, p):
    cnt = 0
    length = len(p)
    for i in range(len(t) - length + 1):
        if t[i:i+length] <= p: cnt += 1
    
    return cnt


def solution(s):
    answer = []
    t = list(s)
    for i in range(len(t)):
        if t[i] in t[:i]:
            answer.append(i-t.index(t[i]))
            t[t.index(t[i])] = '0'
        else:
            answer.append(-1)
    return answer

