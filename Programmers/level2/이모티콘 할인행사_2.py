#DFS 사용버전 

def solution(users, emoticons):
    
    rates_data = []
    fgoal1 = 0
    fgoal2 = 0
    
    def dfs(arr, depth):
        if depth == len(emoticons):
            rates_data.append(arr[:])
            return
        for i in [10, 20, 30, 40]:
            arr[depth] = i
            dfs(arr, depth + 1)
    
    # 1. 모든 할인율 조합을 구한다. (이모티콘의 길이만큼)
    dfs([0] * len(emoticons), 0)
    
    # 2. 할인율의 조합을 순회
    for rates in rates_data:
        goal1 = 0
        goal2 = 0

        for user in users:
            totalpay = 0

            for i in range(len(emoticons)):                            
                if user[0] <= rates[i]:
                    totalpay += emoticons[i] * (100 - rates[i]) / 100 
                                        
            if user[1] <= totalpay:
                goal1 += 1
            else:
                goal2 += totalpay

                                
        if (fgoal1 < goal1) or (fgoal1 == goal1 and fgoal2 < goal2):
            fgoal1 = goal1
            fgoal2 = goal2

    return [fgoal1, fgoal2]