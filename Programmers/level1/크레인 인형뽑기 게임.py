cnt = 0
stack = []

def addToBasket(value):
    global cnt
    global stack

    if stack:
        if value == stack[-1]:
            cnt += 2
            stack.pop()
        else:
            stack. append(value)
    else:
        stack.append(value)
    
    return 0
            
def solution(board, moves):
    global cnt
    global stack
    
    for move in moves:
    
        # 가장 위의 인형 찾기
        for i in range(0, len(board)):
            value = board[i][move-1]
            if value > 0:
                addToBasket(value)
                board[i][move-1] = 0
                break
    
    return cnt
        