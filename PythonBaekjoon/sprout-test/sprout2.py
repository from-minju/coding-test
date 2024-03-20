# #  <<새싹문제>>

# #-----------------------------------
# # :: 배열 ::

# #X보다 작은 수
# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# for i in a:
#     if(i < x):
#         print(i, end=" ")

# #개수 세기
# n = int(input())
# n_list = list(map(int, input().split()))
# v = int(input())
# num = 0
# for i in n_list:
#     if(i == v):
#         num+=1
# print(num)

# #개수 세기 - 이미 있는 count함수 사용하기
# print(n_list.count(v))


#과제 안 내신 분..?
student_num_list = set()
num30 = set({1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30})
for i in range(28):
    student_num_list.add(int(input()))
answer = sorted(list(num30 - student_num_list))
print(answer[0])
print(answer[1])


