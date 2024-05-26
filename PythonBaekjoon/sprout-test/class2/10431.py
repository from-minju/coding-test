# 줄세우기

t = int(input())

for _ in range(t):

    height = list(map(int, input().split()))[1:]
    cnt = 0

    for i in range(20):
        while i>0:
            if height[i] < height[i-1]:
                height[i], height[i-1] = height[i-1], height[i]
                cnt += 1
                i -= 1
            else: break
    
    print(_+1, cnt)



