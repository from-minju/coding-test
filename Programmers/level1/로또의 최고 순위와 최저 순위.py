def solution(lottos, win_nums):
    # {맞춘 번호 수 : 순위}
    dic = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    
    # 0의 개수 
    emptyNum = 0
    lottos.sort()
    for i in lottos:
        if i == 0: emptyNum += 1
        else: break
    
    # 같은 번호의 개수
    equalNum = len(set(win_nums) & set(lottos))
    
    # 결과 리턴
    return [dic[emptyNum + equalNum], dic[equalNum]]