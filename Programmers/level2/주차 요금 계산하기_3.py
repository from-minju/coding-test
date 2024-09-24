
import math

def timeToMin(time):
    h, m = map(int, time.split(':'))
    return h*60 + m


def solution(fees, records):
    MAX_TIME = '23:59'
    answer = []
    dict = {}
    
    # 1. 딕셔너리 만들기 {차량번호 : [시각배열]}
    for record in records:
        time, carnum, inout = record.split(' ')
        if carnum in dict:
            dict[carnum].append(time)
        else:
            dict[carnum] = [time]
    
    
    carnums = sorted(dict.keys()) #['0000', '1234' ....]
    for carnum in carnums:

        # 2. 주차시간 계산하기
        times = dict[carnum] #['06:00', '06:34', '18:59']
        length = len(times)
        sum = 0
        if length % 2 != 0: #홀수개이면 출차된 내역이 없다는 뜻이므로 '23:59'출차로 간주
            times.append(MAX_TIME)
            
        for i in range(0, length, 2):
                sum += timeToMin(times[i+1]) - timeToMin(times[i])
            
        
        # 3. 요금계산
        if sum > fees[0]:
            fee = fees[1] + math.ceil((sum - fees[0]) / fees[2]) * fees[3]
        else:
            fee = fees[1]
        answer.append(fee)
            
    
    return answer