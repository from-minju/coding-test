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
            
