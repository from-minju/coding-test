# 평균
N = int(input())
score_list = list(map(int, input().split()))
score_list.sort()
sum = 0

for i in score_list:
    i = i/score_list[-1]*100
    sum += i

print(sum/len(score_list))

#sum(list) : 리스트의 합을 구하는 함수.
#max(list) : 리스트의 최댓값을 구하는 함수.

#다른 버전 : 원소 하나하나 계산식 적용하지 않아도 됨. 그냥 평균에 계산식 적용한거랑 같음.
# n = int(input())
# arr = list(map(int, input().split()))
# ans = sum(arr) * 100 / max(arr) / n
# print(ans)