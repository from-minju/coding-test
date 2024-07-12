def solution(park, routes):
    h = len(park)
    w = len(park[0])
    loc = [] # 현재위치
    move = {"E": (0,1), "W": (0,-1), "S": (1,0), "N": (-1,0)}
    
    # 1. 시작 위치 찾기
    for x in range(h):
        if "S" in park[x]:
            loc = [x, park[x].index("S")]
            break

    # 2. 이동
    for route in routes:
        op, n = route.split(" ")
        op = move[op]
        n = int(n)

        tx, ty = loc[0], loc[1]

        # 한칸씩 n번 이동해보기 
        for _ in range(n):
            tx += op[0]
            ty += op[1]
            if not (0<= tx < h and 0<= ty < w and park[tx][ty] != "X"): break      
        else:
            loc = [tx, ty]

    return loc

park = ["OOO","OXX","SOO"]
routes = ["E 2","S 2","W 1"]

print(solution(park, routes))
