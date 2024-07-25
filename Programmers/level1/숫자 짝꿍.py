from collections import Counter

def solution(X, Y):
    X = Counter(list(X))
    Y = Counter(list(Y))
    
    mate = list(set(X) & set(Y))
    answer = []
    
    for i in mate:
        n = Y[i] if X[i] > Y[i] else X[i]
        for _ in range(n): answer.append(i) 
    
    answer.sort(reverse = True)
    
    if not answer: return "-1"
    if sum(list(map(int, answer))) == 0: return "0"

    return "".join(answer)
    
    