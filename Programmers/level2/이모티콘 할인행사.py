
SALES = [10, 20, 30, 40]

def solution(users, emoticons):

    fgoal1 = 0
    fgoal2 = 0

    for a in SALES:
        for b in SALES:
            for c in SALES:
                for d in SALES:
                    for e in SALES:
                        for f in SALES:
                            for g in SALES:
                                rates = [a, b, c, d, e, f, g]

                                goal1 = 0
                                goal2 = 0

                                # 각 사람마다 플러스 가입여부 판단 및 이모티콘 판매액 계산
                                for user in users:
                                    totalpay = 0

                                    #모든 이모티콘에 대해 구매여부 판단 
                                    for i in range(len(emoticons)):
                                        # 일정 비율이상 할인하는 이모티콘 모두 구매
                                        if user[0] <= rates[i]:
                                            totalpay += emoticons[i] * (100 - rates[i]) / 100 
                                    
                                    if user[1] <= totalpay:
                                        goal1 += 1
                                    else:
                                        goal2 += totalpay

                                
                                if (fgoal1 < goal1) or (fgoal1 == goal1 and fgoal2 < goal2):
                                    # print(rates, goal1, goal2)
                                    fgoal1 = goal1
                                    fgoal2 = goal2

    return [fgoal1, fgoal2]