# 게임 개발 - 내 답

#input
n, m = map(int, input().split()) #맵의 크기 : 세로n, 가로m
y, x, direction = map(int, input().split()) #현재 나의 위치
maps = []
cnt = 1 #방문한 칸의 수 / 처음에 위치한 곳은 항상 육지이므로 초기값은 1
for i in range(n):
    maps.append(list(map(int, input().split())))

#기본 정보
directions = [0, 1, 2, 3] #북동남서
moves = [(0,-1), (1,0), (0,1), (-1,0)] #북동남서로 앞으로 한칸 움직일때의 변화되는 좌표값
back_moves = [(0,1), (-1,0), (0,-1), (1,0)] #북동남서로 뒤로 한칸 움직일때 변화되는 좌표값

maps[y][x] = 2 #첫시작위치를 이미 간 곳이라고 표시

breakv = 0 #while문 탈출하기 위한 변수, 이동을 멈추기 위한 변수.

while True:

    did_move = 0 #네 방향 중 한곳으로라도 이동했는가? 0:이동안함, 1:이동함
    t_direction = direction 

    for i in range(4): #네 방향을 모두 둘러봄.
        t_direction = directions[t_direction-1] #현재에서 왼쪽돌았을때의 방향을 임시변수에 저장
        tx = x + moves[t_direction][0] #왼쪽으로 한칸 이동했을 때의 위치
        ty = y + moves[t_direction][1] #왼쪽으로 한칸 이동했을 때의 위치
        
        if maps[ty][tx] == 0: #왼쪽방향으로 회전하고 왼쪽으로 한 칸 전진했을 때가 -> 아직 가보지않았고, 육지라면 전진
            direction = t_direction
            cnt += 1 #방문한 칸의 수 1 가
            did_move = 1 #이동했다는 증거.
            x = tx
            y = ty
            maps[y][x] = 2 #이동한 위치를 이미 간 곳이라고 표시.

            break #이동했으면 더이상 둘러볼 필요없으므로 빠져나감.


    #네 방향 모두 이미 가본 칸이거나 바다로 되어있는 경우 == 위의 for문에서 아무런 변화없는 경우
        #if 뒤쪽이동했을때가 바다인 경우: 위치 그대로 움직이지 않음.while문 탈출.
        #else: 한칸뒤로 이동

    if did_move == 0: #네 방향 아무곳도 이동하지 않음.
        tx = x + back_moves[direction][0]
        ty = y + back_moves[direction][1]

        if maps[ty][tx] == 1: #뒤쪽이동햇을때가 바다인 경우
            breakv = 1 #움직임을 멈춤.종료 -> while문 탈출
        else:
            x = tx
            y = ty
    
    if breakv == 1:
        break
    
    
print(cnt)
