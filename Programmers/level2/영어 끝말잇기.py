import math

def solution(n, words):
    
    answer = [0,0]
    
    if len(words[0]) < 2 : 
        answer = [1,1]
    
    list = [words[0]]
    for idx, word in enumerate(words[1:]):
        idx += 1
        
        if (word[0] == words[idx-1][-1]) and (word not in list) and (len(word) >= 2):
            #pass
            list.append(word)
            continue
        else:
            # fail
            num = (idx+1) % n 
            if num == 0:
                num = n
                
            turn = math.ceil((idx+1) / n)

            answer = [num, turn]
            break

        
    return answer

