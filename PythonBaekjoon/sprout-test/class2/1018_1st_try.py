#==체스판 다시 칠하기==
#에러났음. 
N, M = map(int, input().split())
board = []
startsW = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
startsB = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']

#체스판입력받음
for i in range(N):
    board.append(list(input()))

#한줄 안의 값이 맞나 체크하는 함수 -> 리턴값:고쳐야하는횟수(틀린횟수)
def check_by_row (board_cut_list, compare_list):
    global result
    for i in range(8):
        if board_cut_list[i] != compare_list[i]:
            result += 1

def how_many_recoloring (ni, mi):
    #번갈아가며 잘 칠해져있는지 체크 / 기준점 : (ni,mi)
    # global result
    # result = 0
    for i in range(ni,ni+8):
        if i%2==0: #0 또는 짝수행
            if board[ni][mi]=='W': check_by_row(board[i][mi:mi+8], startsW)
            elif board[ni][mi]=='B': check_by_row(board[i][mi:mi+8], startsB)
                
        elif i%2==1:
            if board[ni][mi]=='W': check_by_row(board[i][mi:mi+8], startsB)
            elif board[ni][mi]=='B': check_by_row(board[i][mi:mi+8], startsW)

        
    return result

n =0
m = 0
result_list = []
global result

for ni in range(N-7):
    for mi in range(M-7):
        # print(ni, mi)
        result = 0
        result_list.append(how_many_recoloring(ni,mi))
        # print(result)


result_list.sort()
print(result_list[0])