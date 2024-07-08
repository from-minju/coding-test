def solution(bandage, health, attacks):

    duration = bandage[0]
    recoveryPerSec = bandage[1]
    plusRecovery = bandage[2]
    success = 0
    time = 0
    maxHealth = health

    # 1. attack : [공격시간, 피해량]
    for attack in attacks:
        atime = attack[0]
        aamount = attack[1]
        # 1. 공격 전까지의 상황 update
        beforeTime = max(0, atime - time - 1)
        success += beforeTime #연속성공누적수
        health += recoveryPerSec * beforeTime
        health = min(maxHealth, health)

        sCount = success // duration # 추가체력 얻을 수 있는 횟수
        if(sCount >= 1):
            health += plusRecovery * sCount
            health = min(maxHealth, health)

            # success -= sCount * duration
            success = success % duration

        time = atime

        # 2. 공격 처리 
        success = 0
        health -= aamount
        if health<=0: return -1

    return health

# [5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]

bandage = [5, 1, 5]
health = 30
attacks = [[2, 10], [9, 15], [10, 5], [11, 5]]
result = solution(bandage, health, attacks)
print(result)



