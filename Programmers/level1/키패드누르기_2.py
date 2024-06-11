# 키패드 누르기_2

def solution(numbers, hand):
    answer = ''
    # 각 기패드 번호의 좌표를 담은 딕셔너리
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0), 0:(3,1),'#':(3,2)}

    left = [1,4,7] #왼손을 사용해야하는 번호
    right = [3,6,9] #오른손을 사용해야하는 번호

    #오른손과 왼손 시작위치 초기화
    left_hand = '*'
    right_hand = '#'

    # 누른 번호 순서대로 탐색
    for num in numbers:
        # 1,4,7 누른 경우 -> 왼손
        if num in left:
            answer += 'L'
            left_hand = num
        # 3,6,9 누른 경우 -> 오른손
        elif num in right:
            answer += 'R'
            right_hand = num
        #가운데 2,5,8,0 누른 경우
        else:
            curPos = key_dict[num] #현재 누른 번호의 좌표
            lPos = key_dict[left_hand] #현재 왼손의 위치
            rPos = key_dict[right_hand] #현재 오른손의 위치

            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1]) #오른손으로 누를 경우 거리
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1]) #왼손으로 누를 경우 거리

            # 왼손이 더 가까이 있음
            if ldist < rdist:
                answer += 'L'
                left_hand = num
            # 오른손이 더 가까이 있음
            elif ldist > rdist:
                answer += 'R'
                right_hand = num
            # 왼손과 오른손의 거리가 같음
            else:
                # 왼손잡이인 경우
                if hand == 'left':
                    answer += 'L'
                    left_hand = num
                # 오른손잡이인 경우
                else:
                    answer += 'R'
                    right_hand = num

    return answer