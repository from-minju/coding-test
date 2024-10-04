
from collections import deque

def solution(n, t, m, timetable):
    
    def timeToMin(time):
        h, m = map(int, time.split(':'))
        return h*60 + m
    
    def minToTime(min):
        h = min // 60
        m = min - h*60
        return getTimeFormatted(h) + ':' + getTimeFormatted(m)
            
    def getTimeFormatted(t):
        if t < 10:
            t = "0" + str(t)
        else:
            t = str(t)
        return t
    
    # timetable 정렬
    timetable.sort()
    # timetable HH:MM -> 분단위로 변환
    for i in range(len(timetable)):
        timetable[i] = timeToMin(timetable[i])
    # deque로 변환 
    timetable = deque(timetable)

    dep_time = timeToMin("9:00")
    bus_time = []
    psgr_data = {}
    
    # 딕셔너리 만들기 
    for i in range(n):
        # bus_time.append(dep_time)
        psgr_data[dep_time] = []
        psgr_num = 0
    
        while timetable:

            # 셔틀 1회당 최대 인원보다 더 많이 탄 경우 그만 태움.
            if psgr_num >= m:
                break
            # 출발시간 이전에 도착한 승객만 태움.
            if dep_time >= timetable[0]:
                temp = timetable.popleft()
                psgr_data[dep_time].append(temp)
                psgr_num += 1
            else:
                break
        
        dep_time += t

    # 버스 출발시간표 배열 만들기
    bus_time = sorted(psgr_data.keys())

    # 가장 늦은 시간 구하기
    corn_time = 0
    last_time = bus_time[-1]

    if len(psgr_data[last_time]) < m:
        corn_time = last_time
    else:
        corn_time = psgr_data[last_time][-1] - 1 #자리가 없다면 : (그 타임에 가장 늦게 도착하는 사람의 시간) - 1

            
    return minToTime(corn_time)
