# 블랙잭 - 다른 코드


n, m = map(int, input().split())
data = sorted(list(map(int, input().split())), reverse=True)
biggest = 0

for x in range(0, n-2):
    for y in range(x+1, n-1):
        for z in range(y+1, n):
            temp = data[x] + data[y] + data[z]
            if temp <= m:
                if temp > biggest:
                    biggest = temp
                break
                

print(biggest)



#블랙잭 다른 코드 
# n, m = map(int, input().split())
# data = sorted(list(map(int, input().split())))
# biggest = 0

# for x in range(0, n-2):
#     for y in range(x+1, n-1):
#         for z in range(y+1, n):
#             temp = data[x] + data[y] + data[z]
#             if temp <= m:
#                 if temp > biggest:
#                     biggest = temp
#                           
# print(biggest)
