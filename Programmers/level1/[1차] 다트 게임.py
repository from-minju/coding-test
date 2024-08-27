def solution(dartResult):
    result = []
    idx = -1
    bonus = {"S":1, "D":2, "T":3}
    
    dartResult = dartResult.replace("10", "@")
    
    for dart in dartResult:
        if dart == "@":
            dart = '10'
            
        if dart.isdigit():
            idx += 1
            result.append(int(dart))
        elif dart in bonus:
            result[idx] = result[idx] ** bonus[dart]
        elif dart == '*':
            result[idx] *= 2
            if idx != 0: result[idx - 1] *= 2
        elif dart == '#':
            result[idx] *= -1
    
    return sum(result)


# error

def solution(dartResult):
    result = [0,0,0]
    idx = -1
    bonus = {"S":1, "D":2, "T":3}
    
    # 1. 전처리 (입력을 리스트로 분리하기)
    if "10" in dartResult:
        a, b = map(list, dartResult.split("10"))
        dartResult = a + ['10'] + b
    else:
        dartResult = list(dartResult)

    # 2. 
    for dart in dartResult:
        if dart.isdigit():
            idx += 1
            result[idx] = int(dart)
        elif dart in bonus:
            result[idx] = result[idx] ** bonus[dart]
        elif dart == '*':
            result[idx] *= 2
            if idx != 0: result[idx - 1] *= 2
        elif dart == '#':
            result[idx] *= -1
    
    return sum(result)
            
        
def solution(dartResult):
    result = [0,0,0]
    idx = -1
    bonus = {"S":1, "D":2, "T":3}
    
    for i in range(len(dartResult)):
        dart = dartResult[i]
        if dart.isdigit():
            idx += 1
            if dartResult[i+1] == '0':
                result[idx] = 10
                i += 1
                continue
            else: result[idx] = int(dart)
        elif dart in bonus:
            result[idx] = result[idx] ** bonus[dart]
        elif dart == '*':
            result[idx] *= 2
            if idx != 0: result[idx - 1] *= 2
        elif dart == '#':
            result[idx] *= -1
    
    return sum(result)
