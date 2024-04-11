# 게임 개발 - 내 답

#input
n, m = map(int, input().split())
x, y, direction = map(int, input().split())
maps = []
cnt = 1 #방문한 칸의 수 / 처음에 위치한 곳은 항상 육지이므로 초기값은 1
for i in range(n):
    maps.append(list(map(int, input().split())))

#기본 정보
directions = [0, 1, 2, 3]
moves = [(0,-1), (1,0), (0,1), (-1,0)]
back_moves = [(0,1), (-1,0), (0,-1), (1,0)]

breakv = 0

while True:

    can_move = 0
    t_direction = direction

    for i in range(4): #네 방향을 모두 둘러봄. 1, 2, 3, 4
        t_direction = directions[t_direction-1]
        print("--[{0}번째 탐색] 방향:{1}".format(i+1, t_direction))
        tx = x + moves[t_direction][0]
        ty = y + moves[t_direction][1]
        
        if maps[ty][tx] == 0: #왼쪽방향으로 회전하고 왼쪽으로 한 칸 전진했을 때가 -> 아직 가보지않았고, 육지라면 전진
            direction = t_direction
            maps[y][x] = 2 #이미 간 곳이라고 표시.
            cnt += 1 #방문한 칸의 수 1 가
            can_move = 1 #이동했다는 증거.
            x = tx
            y = ty

    #네 방향 모두 이미 가본 칸이거나 바다로 되어있는 경우 == 위의 for문에서 아무런 변화없는 경우
        #if 뒤쪽이동했을때가 바다인 경우: 위치 그대로 움직이지 않음.while문 탈출.
        #else: 한칸뒤로 이동

    if can_move == 0:
        tx = x + back_moves[direction][0]
        ty = y + back_moves[direction][1]

        if maps[ty][tx] == 1: #뒤쪽이동햇을때가 바다인 경우
            breakv = 1
        else:
            x = tx
            y = ty
    
    if breakv == 1:
        break
    

print(cnt)
    