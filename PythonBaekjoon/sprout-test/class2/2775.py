# 2775. 부녀회장이 될테야


t = int(input())

for _ in range(t):

    k = int(input())
    n = int(input())

    data = [[0]*(n+1) for _ in range(k+1)] #2차원배열 초기화 - k행, n열

    #2차원배열 채우기
    for i in range(k+1):
        for j in range(1, n+1):
            if i==0: 
                data[i][j]=j
            else:
                sum = 0
                for y in range(1, j+1):
                    sum += data[i-1][y]
                data[i][j] = sum

    print(data)

    


# def how_many (k, n):

#     global sum

#     if k==0: 
#         sum = n
#     else:

#         for i in range(k):
#             for j in range(1, n+1):
#                 sum += how_many(i, j)
        
#     return sum


# t = int(input())

# for _ in range(t):

#     k = int(input())
#     n = int(input())

#     sum = 0

#     print(how_many(k, n))



'''
a층 b호 : (a-1)층의 1호~b호까지 사람들 수의 합
0층부터, 1호부터 있음.
0층 i호 : i명
k층 n호에는 몇명의 사람이?
'''