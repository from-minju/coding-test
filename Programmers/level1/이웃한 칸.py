'''
위,아래,오,왼 - 같은 색의 칸 개수
'''

def solution(board, h, w):
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    l = len(board)
    count = 0
    
    for i in range(4):
        tx = h + dx[i]
        ty = w + dy[i]
        
        if (0<= tx < l and 0<= ty < l):
            if(board[tx][ty] == board[h][w]):
                count += 1
        else:
            continue        
    
    return count
        

board = [["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]]
h = 1
w = 1

print(solution(board, h, w))
        