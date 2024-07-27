def solution(s, skip, index):
    
    alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    alphabets = list(filter(lambda x: not x in skip, alphabets))
    answer = ''
    
    for x in s:
        idx = alphabets.index(x) + index
        if idx >= len(alphabets): 
            idx = idx % len(alphabets) 
        answer += (alphabets[idx])
    
    return answer