def solution(survey, choices):
    
    scoreDic = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    choiceDic = {1:[0,3], 2:[0,2], 3:[0,1], 4:[0,0], 5:[1,1], 6:[1,2], 7:[1,3]}
    types = ["RT", "CF", "JM", "AN"]
    result = ''
    
    # 유형별 점수 계산
    for i in range(len(survey)):
        choice = choices[i]
        type, score = choiceDic[choice]
        type = survey[i][type]
        
        # 점수 반영
        scoreDic[type] += score
        
    # 유형 결정
    for t in types:
        a = t[0]
        b = t[1]
        scoreA = scoreDic[a]
        scoreB = scoreDic[b]
            
        if scoreA < scoreB: result += b
        else: result += a
            
            
    return result
