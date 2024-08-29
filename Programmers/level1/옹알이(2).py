def solution(babbling):
    answer = 0
    
    for word in babbling:
        word = word.replace("aya", "1")
        word = word.replace("ye", "2")
        word = word.replace("woo", "3")
        word = word.replace("ma", "4")
        
        if word.isdigit():
            for i in range(len(word)-1):
                if word[i] == word[i+1]: break
            else:
                answer += 1
            continue
        else:
            continue  
        
    return answer


