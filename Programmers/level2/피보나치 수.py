def solution(n):
    
    maps = {0:0, 1:1}
    
    for x in range(2, n+1):
        maps[x] = maps[x-1] + maps[x-2]
    
    return maps[n] % 1234567
        
        