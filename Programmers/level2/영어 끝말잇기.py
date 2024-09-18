import math

def solution(n, words):
    
    answer = [0,0]
    
    # 첫번째 단어 길이 체크
    if len(words[0]) < 2 : 
        answer = [1,1]
    
    # 이전에 등장한 단어 리스트에 첫번째 단어를 추가
    list = [words[0]]

    # 2번째 단어부터 끝말잇기의 3가지 조건 검사
    for idx, word in enumerate(words[1:]):
        idx += 1
        
        # 1. 앞사람이 말한 단어의 마지막 문자로 시작하는가 / 2. 이전에 등장하지 않은 단어인가 / 3. 단어길이가 두글자 이상인가 
        if (word[0] == words[idx-1][-1]) and (word not in list) and (len(word) >= 2):
            # 끝말잇기에 통과한 경우
            list.append(word)
            continue
        else:
            # 끝말잇기에 실패한 경우 
            num = (idx+1) % n 
            if num == 0:
                num = n
                
            turn = math.ceil((idx+1) / n)

            answer = [num, turn]
            break

        
    return answer

# 실수한 부분 : 10번째줄, idx+1안한거