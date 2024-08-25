def solution(t, p):
    cnt = 0
    length = len(p)
    for i in range(len(t) - length + 1):
        if t[i:i+length] <= p: cnt += 1
    
    return cnt

