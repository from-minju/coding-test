def solution(wallpaper):
    
    h = len(wallpaper)
    w = len(wallpaper[0])
    
    sx = h-1
    sy = w-1
    ex = 0
    ey = 0
    
    for x in range(h):
        for y in range(w):
            if wallpaper[x][y] == "#":
                if sx > x: sx = x
                if ex < x: ex = x
                if sy > y: sy = y
                if ey < y: ey = y
    
    return [sx, sy, ex+1, ey+1]