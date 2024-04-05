#==체스판 다시 칠하기==
N, M = map(int, input().split())
board = []

#체스판입력받음
for i in range(N):
    board.append(list(input()))

result = []

for ni in range(N-7):
    for mi in range(M-7):
        
        w_index = 0
        b_index = 0
        count = 0

        for i in range(ni, ni+8):
            for j in range(mi, mi+8):
                if board[ni][mi] == 'W':
                    if(i+j)%2==0:
                        if board[i][j]!='W': count+=1
                    elif(i+j)%2==1:
                        if board[i][j]!='B': count+=1   
                elif board[ni][mi] == 'B':
                    if(i+j)%2==0:
                        if board[i][j]!='B': count+=1
                    elif(i+j)%2==1:
                        if board[i][j]!='W': count+=1   

    result.append(count)

result.sort()
print(result[0])
