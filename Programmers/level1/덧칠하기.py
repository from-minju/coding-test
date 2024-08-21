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


def solution0(n, m, section):
    cnt = 0
    t = 0
    
    for sec in section:
        if sec < t:
            continue
        else:
            cnt += 1
            t = sec + m
    
    return cnt

# 다른 풀이
def solution2(n, m, section):
    answer = 1
    prev = section[0]
    for sec in section:
        if sec - prev >= m:
            prev = sec
            answer += 1

    return answer