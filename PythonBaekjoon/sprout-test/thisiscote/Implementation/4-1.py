#상하좌우 - 내 답

n = int(input())
move = input().split()
x=1
y=1
tx=1
ty=1
for i in move:
    if i=='L':
        ty = y-1
    elif i=='R':
        ty = y+1
    elif i=='U':
        tx = x-1
    elif i=='D':
        tx = x+1

    if (1<=tx<=n and 1<=ty<=n):
        y = ty
        x = tx
    
print(x, y)
