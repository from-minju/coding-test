from datetime import datetime

# 시간차이를 계산하는 함수
def get_time_difference(time1, time2):
    # 문자열을 datetime 객체로 변환
    time_format = "%H:%M"
    time1 = datetime.strptime(time1, time_format)
    time2 = datetime.strptime(time2, time_format)

    # 시간 차이 계산
    time_difference = time2 - time1

    # 시간 차이를 분 단위로 변환
    minutes_difference = time_difference.total_seconds() / 60

    return int(minutes_difference)


def solution(plans):
    answer = []
    stack = []
    
    # 시간 순서대로 정렬
    plans = sorted(plans, key=lambda x: datetime.strptime(x[1], "%H:%M"))

    # 마지막요소 빼고 탐색 (마지막 요소는 시간제한이 없으므로)
    for idx in range(len(plans) - 1):
        
        # 다음 과제까지 남은 시간 계산
        psb_time = get_time_difference(plans[idx][1], plans[idx+1][1])

        # 현재요소 스택에 추가 (과목, 과제남은시간)
        stack.append((plans[idx][0], plans[idx][2]))
        
        # 시간이 남았다면
        while psb_time > 0 and stack:
            iname, itime = stack.pop() # 가장 최근의 과제를 불러옴
            itime = int(itime)
            # 남은 시간 동안 과제를 다 끝내지 못했을 때
            if psb_time < itime:
                itime -= psb_time
                stack.append((iname, itime))
                break
            # 남은 시간동안 과제를 끝냈을 경우
            else:
                answer.append(iname)
                psb_time -= itime
                
    # 마지막 요소를 스택에 추가           
    stack.append((plans[-1][0], plans[-1][2]))
    
    # 스택에 남아있는 과제들을 해결
    while stack:
        iname, itime = stack.pop()
        answer.append(iname)
            
          
    return answer