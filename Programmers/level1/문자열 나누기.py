def solution(s):

    result = 0
    xCnt = 0 # x가 나온 횟수
    yCnt = 0 # x가 아닌 다른 글자들이 나온 횟수
    
    # 문자열의 남은 부분이 없으면 종료
    while s:
        
        x = s[0]
        
        for idx,i in enumerate(s):
            if x == i:
                xCnt += 1
            else:
                yCnt += 1
            
            if xCnt == yCnt:
                result += 1
                s = s[idx+1:]
                break
        # 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없으면 종료
        else:
            result += 1
            break
        
    return result 
        