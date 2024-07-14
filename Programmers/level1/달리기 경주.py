# def solution(players, callings):
    
#     for calling in callings:
#         idx = players.index(calling)
#         players[idx], players[idx-1] = players[idx-1], players[idx]
    
#     return players



def solution(players, callings):
    # players를 딕셔너리로 변경 {이름: 인덱스}
    dic = {player: idx for idx, player in enumerate(players)}
    # dic = {}
    # for idx, player in enumerate(players):
    #     dic[player] = idx
    
    # callings 한 명씩 처리 (앞뒤 자리 이동)
    for calling in callings:
        idx = dic[calling]

        # 바뀐 players 인덱스 dic에 반영해줘야함.
        dic[calling] -= 1
        dic[players[idx-1]] += 1 

        players[idx], players[idx-1] = players[idx-1], players[idx]
        
    
    return players

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

print(solution(players, callings))