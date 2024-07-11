''' 1:47
유저 - 한번에 1유저 신고 가능 
동일유저 여러번 신고해도 신고횟수는 1회로 처리됨.

k번 이상 신고된 유저 - 정지
이 유저를 신고한 모든 유저에게 메일로 정지사실 알림.


필요한 변수
- 유저 ID
- 유저별, 유저가 신고한 ID 목록 -> 신고당한 유저 : 신고한 사람
- 유저별 신고당한 횟수

알고리즘
1. 신고 처리 (한 사람이 한사람 신고 1번밖에 처리 안됨.)
2. k번 이상 신고당한 유저 정지처리
3. 정지당한유저를 신고한 유저에게 메일로 알림처리 
4. 메일 받은 횟수 return 
1:55
'''
def solution(id_list, report, k):
    l = len(id_list)
    reported = [[] for _ in range(l)]
    result = [0 for _ in range(l)]
    id = {}
    for i in range(l):
        id[id_list[i]] = i
    
    # 1. 신고 처리
    # 신고당한사람 [신고한 사람1, 2, ...]
    for str in report:
        a, b = str.split(" ")
        
        if a in reported[id[b]]:
            continue
        else:
            reported[id[b]].append(a)
    
    # 2. 정지 처리 (k번 이상 신고당한 사람)
    for arr in reported:
        if len(arr) >= k:
            for user in arr:
                result[id[user]] += 1
            
    
    return result