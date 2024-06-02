from datetime import datetime

def get_time_difference(time1, time2):
    # 문자열을 datetime 객체로 변환
    time_format = "%H:%M"
    time1 = datetime.strptime(time1, time_format)
    time2 = datetime.strptime(time2, time_format)

    # 시간 차이 계산
    time_difference = time2 - time1

    # 음수인 경우 (시간 b가 더 이른 시간인 경우) 차이를 양수로 만들기 위해 절대값을 취함
    if time_difference.days < 0:
        time_difference = -time_difference

    # 시간 차이를 분 단위로 변환
    minutes_difference = time_difference.total_seconds() / 60

    return int(minutes_difference)


def solution(plans):
    answer = []
    stack = []
    
    for idx in range(len(plans) - 1):
        
        psb_time = get_time_difference(plans[idx][1], plans[idx+1][1])
        stack.append((plans[idx][0], plans[idx][2])) #(과목, 과제남은시간)
        
        while psb_time > 0 and stack:
            iname, itime = stack.pop()
            if psb_time < itime:
                itime -= psb_time
                stack.append((iname, itime))
                break
            else:
                answer.append(iname)
                psb_time -= itime
                
                
    stack.append((plans[-1][0], plans[-1][2]))
    
    while stack:
        iname, itime = stack.pop()
        answer.append(iname)
            
          
    return answer