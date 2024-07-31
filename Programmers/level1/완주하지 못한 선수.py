def solution(participant, completion):
    # 리스트 정렬
    participant.sort()
    completion.sort()
    
    # 없는 사람 찾기
    for i in range(len(participant) - 1):
        if participant[i] != completion[i]:
            return participant[i]
    
    # 예외처리 - 완주하지 못한 선수가 맨 마지막에 있는 경우 
    return participant[len(participant) - 1]


# 2. Counter사용 
import collections
def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


# 3. hash 함수 사용
def solution(participant, completion):
    sum = 0
    dic = {}

    # 1. 딕셔너리 만들기 / 2. hash값의 합 sum 구하기
    for part in participant:
        dic[hash(part)] = part
        sum += int(hash(part))

    # 3. completion의 sum(hash) 빼기
    for comp in completion:
        sum -= hash(comp)

    return dic[sum]

