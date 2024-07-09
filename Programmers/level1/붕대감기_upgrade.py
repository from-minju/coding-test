'''
# bandage : [시전 시간, 초당 회복량, 추가 회복량]
# health : 최대 체력
# attacks : 몬스터의 [공격 시간, 피해량]
'''
def solution(bandage, health, attacks):
    castingTime = bandage[0]
    recoveryPerSec = bandage[1]
    bonusRecovery = bandage[2]

    success = 0 # 연속 성공 시간
    time = 0 # 이전 공격을 만난 시간
    maxHealth = health

    # 1. attack : [공격시간, 피해량]
    for attack in attacks:

        attackTime = attack[0] # 공격시간
        attackAmount = attack[1] # 피해량

        # 1. 공격 전까지의 상황 update
        beforeTime = max(0, attackTime - time - 1)
        success += beforeTime #연속성공누적수
        health += recoveryPerSec * beforeTime
        health = min(maxHealth, health)

        #   추가체력 처리
        sCount = success // castingTime # 추가체력 얻을 수 있는 횟수
        if(sCount >= 1):
            health += bonusRecovery * sCount
            health = min(maxHealth, health)
            success = success % castingTime

        # 2. 공격 처리 
        success = 0
        health -= attackAmount
        if health<=0: return -1


        time = attackTime

    return health

# [5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]

bandage = [5, 1, 5]
health = 30
attacks = [[2, 10], [9, 15], [10, 5], [11, 5]]
result = solution(bandage, health, attacks)
print(result)



