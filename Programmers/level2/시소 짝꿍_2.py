from collections import Counter

def solution(weights):
    cnt = 0
    weights.sort()
    counter = Counter(weights)

    for i in range(len(weights) - 1):
        w = weights[i]
        
        cnt += counter[w] - 1
        cnt += counter[2*w]
        cnt += counter[3*w / 2]
        cnt += counter[4*w / 3]
        
        counter[w] -= 1
        
    return cnt