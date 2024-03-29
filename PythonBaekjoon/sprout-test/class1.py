#별 찍기 2
x = int(input())
for i in range(x):
    for a in range(x-i-1):
        print(" ",end='')
    for b in range(i+1):
        print("*", end='')
    print()

단어의 개수
strings = input()
words_list = strings.split() #split()과 split('')의 차이
print(len(words_list))


# #단어 공부
ex = list(input())
alp_dic = {}
for i in ex:
    i = i.upper()
    if(i in alp_dic):
        alp_dic[i] += 1
    else:
        alp_dic[i] = 1

num = 0
result = ''
for i in alp_dic:
    if(num < alp_dic[i]):
        num = alp_dic[i]
        result = i
    elif(num > alp_dic[i]):
        continue
    else: # num == alp_dic[i]
        result = '?'

print(result)


#최댓값
ans_list = []
for i in range(9):
    ans_list.append(int(input()))
ans_list_sorted = sorted(ans_list)
print(ans_list_sorted[-1])
print(ans_list.index(ans_list_sorted[-1])+1)


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

#==3/28(목)==
#문자열 반복
t = int(input())
for i in range(t):
    r, s = input().split()
    r = int(r)
    s = list(s)
    for char in s:
        for i in range(r):
            print(char, end='')
    print()

#문자열 반복 - string도 리스트처럼 s[i]가 가능함. *연산자로 문자반복도 가능함. 
t = int(input())
for i in range(t):
    r, s = input().split()
    for i in range(len(s)):
        print(int(r) * s[i], end='')
    print()


#알람 시계
h, m = map(int, input().split())

if m-45 < 0:
    if h==0: h=23
    else: h = h-1
    m = 60 + (m-45)
else:
    m = m - 45
print(h, m)

#알람 시계 - 틀린버전 : 반례 (입력 : 0, 50) -> (출력 : 24, 5) (정답출력 : 0 5)
h, m = map(int, input().split())
if h==0: h=24
total = h *60 + m - 45
h = total//60
m = total%60
print(h, m)

#알람시계 - 위에거 고친 버전
h, m = map(int, input().split())
total = h *60 + m - 45
if total<0:
    total += 24 * 60
h = total//60
m = total%60
print(h, m)


#음계
scale = input().split()
if (scale[0] < scale[1]): result = "ascending"
else : result = "descending"
for i in range(1, len(scale)-1):
    if scale[i] < scale[i+1]: temp_result = "ascending"
    else: temp_result = "descending"   
    if(temp_result != result):
        result = "mixed"
        break
    else:
        result = temp_result
print(result)

#음계 - 훨~씬 더 간단한 방법...
i = input()
if i == '1 2 3 4 5 6 7 8': print('ascending')
elif i == '8 7 6 5 4 3 2 1': print('descending')
else: print('mixed')

#나머지
num_list = []
for i in range(10):
    num_list.append(int(input()))

ans = set()
for i in num_list:
    ans.add(i%42)
print(len(ans))

#나머지_더 간단ver.
ans = set()
for _ in range(10):
    ans.add(int(input()) % 42)
print(len(ans))


#O, X퀴즈
n = int(input())

for _ in range(n):
    score_list = list(input())

    acc_score = 0
    total_score = 0

    for score in score_list:
        if score == "O":
            if acc_score > 0:
                acc_score += 1
            else:
                acc_score = 1
        elif score == "X":
            acc_score = 0

        total_score += acc_score
    
    print(total_score)

