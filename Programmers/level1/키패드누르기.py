# 키패드 누르기

from collections import deque

# 키패드 번호간의 거리를 구해 리턴하는 함수 - BFS
def get_distance(start, end):
    visited = [[0 for _ in range(3)] for _ in range(4)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = 1 # 시작위치 방문처리
    
    while q:
        x, y = q.popleft()
        
        # (x,y)가 end인 경우
        if x == end[0] and y == end[1]:
            return visited[x][y] - 1
        
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            
            # 이동했을 때의 위치가 키패드 범위 내에 있고 방문하지 않은 경우
            if (0<= tx <=2 and 0<=ty<=2) or (tx==3 and ty==1):
                if visited[tx][ty] == 0:
                    q.append((tx,ty))
                    visited[tx][ty] = visited[x][y] + 1
                    
    return 0
            
        
    
    
def solution(numbers, hand):
    answer = ''
    # 각 기패드 번호의 좌표를 담은 딕셔너리
    keypads = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2), 0:(3,1)}
    
    # 현재 오른손과 왼손의 위치 - 시작 위치로 초기화
    right_hand = (3,2)
    left_hand = (3,0)
    
    # 누른 번호 순서대로 탐색
    for num in numbers:

        #현재 누른 번호의 좌표(위치)
        num_loc = keypads[num]
        
        # 1,4,7 누른 경우 -> 왼손
        if num_loc[1] == 0:
            answer += "L"
            left_hand = num_loc
        # 3,6,9 누른 경우 -> 오른손
        elif num_loc[1] == 2:
            answer += "R"
            right_hand = num_loc
        #가운데 2,5,8,0 누른 경우
        else:
            rdist = get_distance(right_hand, num_loc) #오른손으로 누를 경우 거리
            ldist = get_distance(left_hand, num_loc) #왼손으로 누를 경우 겨리
            
            # 왼손이 더 가까이 있음
            if rdist > ldist:
                answer += "L"
                left_hand = num_loc
            # 오른손이 더 가까이 있음
            elif rdist < ldist:
                answer += "R"
                right_hand = num_loc
            # 왼손과 오른손의 거리가 같음
            else:
                # 오른손잡이인 경우
                if hand == "right":
                    answer += "R"
                    right_hand = num_loc
                # 왼손잡이인 경우
                elif hand == "left":
                    answer += "L"
                    left_hand = num_loc
    return answer