from datetime import datetime
import math

def solution(fees, records):
    fmt = '%H:%M'
    MAX_TIME = datetime.strptime('23:59', fmt)
    answer = []
    map = {}
    
    # 1. 맵 만들기 {차량번호 : [시각배열]}
    for record in records:
        time, carnum, inout = record.split(' ')
        
        time = datetime.strptime(time, fmt)

        if carnum in map:
            map[carnum].append(time)
        else:
            map[carnum] = [time]
    
    # 2. 주차시간 계산하기
    carnums = sorted(map.keys())
    
    for carnum in carnums:
        times = map[carnum]
        length = len(times)
        sum = 0
        if length % 2==0:
            for i in range(0, length, 2):
                sum += int((times[i+1] - times[i]).total_seconds() / 60)
        else:
            for i in range(0, length-1, 2):
                sum += int((times[i+1] - times[i]).total_seconds() / 60)       
            sum += int((MAX_TIME - times[-1]).total_seconds() / 60)
            
        
        # 3. 요금계산
        if sum > fees[0]:
            fee = fees[1] + math.ceil((sum - fees[0]) / fees[2]) * fees[3]
        else:
            fee = fees[1]
        answer.append(fee)
            
    
    
    
    return answer