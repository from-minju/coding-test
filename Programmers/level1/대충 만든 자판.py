def solution(keymap, targets):
    dic = {"A":0, "B":0, "C":0, "D":0, "E":0, "F":0, "G":0, "H":0, "I":0, "J":0, "K":0, "L":0, "M":0, "N":0, "O":0, "P":0, "Q":0, "R":0, "S":0, "T":0, "U":0, "V":0, "W":0, "X":0, "Y":0, "Z":0}
    answer = []
    
    # 알파벳마다 최소 몇번 눌러야 하는지 딕셔너리에 저장
    for str in keymap:
        for idx, char in enumerate(str):
            if dic[char] == 0: 
                dic[char] = idx + 1
            else:
                dic[char] = min(dic[char], idx + 1)
    
    # target 문자열 최소 몇번 눌러야 하는지 계산하기
    for target in targets:
        sum = 0
        for char in target:
            if dic[char] == 0:
                answer.append(-1)
                break
            else:
                sum += dic[char]
        else:
            answer.append(sum)
    
    return answer