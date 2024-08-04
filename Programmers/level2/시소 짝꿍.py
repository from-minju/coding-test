# 실패 (시간 초과)
def solution(weights):
    cnt = 0
    weights.sort()

    for i in range(len(weights) - 1):
        for j in range(i+1, len(weights)):
            a = weights[i]
            b = weights[j]

            if a == b: cnt += 1 
            elif b == 2*a: cnt += 1
            elif b == 3*a / 2: cnt += 1
            elif b == 4*a / 3: cnt += 1

    return cnt