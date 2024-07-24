def solution(n, lost, reserve):
    temp = set(lost) & set(reserve)
    lost = list(set(lost) - temp)
    reserve = list(set(reserve) - temp)

    
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
            
    cnt = n - len(lost)
    
    return cnt