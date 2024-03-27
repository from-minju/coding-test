# #별 찍기 2
# x = int(input())
# for i in range(x):
#     for a in range(x-i-1):
#         print(" ",end='')
#     for b in range(i+1):
#         print("*", end='')
#     print()

#단어의 개수
# strings = input()
# words_list = strings.split() #split()과 split('')의 차이
# print(len(words_list))


# # #단어 공부
# ex = list(input())
# alp_dic = {}
# for i in ex:
#     i = i.upper()
#     if(i in alp_dic):
#         alp_dic[i] += 1
#     else:
#         alp_dic[i] = 1

# num = 0
# result = ''
# for i in alp_dic:
#     if(num < alp_dic[i]):
#         num = alp_dic[i]
#         result = i
#     elif(num > alp_dic[i]):
#         continue
#     else: # num == alp_dic[i]
#         result = '?'

# print(result)


# #최댓값
# ans_list = []
# for i in range(9):
#     ans_list.append(int(input()))
# ans_list_sorted = sorted(ans_list)
# print(ans_list_sorted[-1])
# print(ans_list.index(ans_list_sorted[-1])+1)


#숫자의 개수
A = int(input())
B = int(input())
C = int(input())

mul_list = list(str(A*B*C))
result = [0,0,0,0,0,0,0,0,0,0]
for i in mul_list:
    result[int(i)] += 1
for i in result:
    print(i)
