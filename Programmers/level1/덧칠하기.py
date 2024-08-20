# 덧칠하기
def solution(n, m, section):
    cnt = 0
    length = len(section)
    t = 0

    for i in range(0, length):
        if section[i] < t:
            continue
        else:
            cnt += 1
            t = section[i] + m
    
    return cnt