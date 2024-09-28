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
    corn_time = dep_time
    
    # 셔틀 운행 횟수만큼 for문
    for i in range(n):
        psgr_num = 0
        
        # 셔틀 1회당 탈 수 있는 사람 처리
        while timetable:
            # 셔틀 1회당 최대 인원보다 더 많이 탄 경우 그만 태움.
            if psgr_num > m:
                break
            # 출발시간 이전에 도착한 승객만 태움.
            if dep_time >= timetable[0]:
                timetable.popleft()
                psgr_num += 1
        
        if psgr_num < m:
            corn_time = dep_time
        
        dep_time += t
        
    return minToTime(corn_time)
        
    