#  <<새싹문제>>

#-----------------------------------
# :: 배열 ::

#X보다 작은 수
n, x = map(int, input().split())
a = list(map(int, input().split()))
for i in a:
    if(i < x):
        print(i, end=" ")

#개수 세기
n = int(input())
n_list = list(map(int, input().split()))
v = int(input())
num = 0
for i in n_list:
    if(i == v):
        num+=1
print(num)

#개수 세기 - 이미 있는 count함수 사용하기
print(n_list.count(v))


#과제 안 내신 분..?
student_num_list = set()
num30 = set({1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30})
for i in range(28):
    student_num_list.add(int(input()))
answer = sorted(list(num30 - student_num_list))
print(answer[0])
print(answer[1])


#행렬 덧셈
n, m = map(int, input().split()) #n이 행, m이 열

list_a = []
list_b = []

for row in range(n):
    row = list(map(int, input().split()))
    list_a.append(row)

for row in range(n):
    row = list(map(int, input().split()))
    list_b.append(row)

for row in range(n):
    for column in range(m):
        print(list_a[row][column] + list_b[row][column], end=" ")
    print()

#-----------------------------------
# :: 문자열 ::

#아스키 코드 - ord() : 문자의 아스키 코드값을 리턴하는 함수
asc = input()
print(ord(asc))

#단어 길이 재기
string = input()
print(len(string))

#대소문자 바꾸기
#string.isupper() : 대문자인지 True/False
#string.lower() : 소문자로
string = list(input())
for i in string:
    if i.isupper(): i = i.lower()
    else: i = i.upper()
    print(i, end="")

#input()과 for문
i = input()
for i in string: #string을 for문에 넣으면 에러발생!
    print(i)

for i in input(): #for문에 바로 input()바로 넣으면 에러발생안함. 
    print(i)

#대소문자 바꾸기 - swapcase()함수 활용하기
print(input().swapcase())

#학점계산
grade = input()
dic = {'A+':'4.3', 'A0':'4.0', 'A-':'3.7',
       'B+':'3.3', 'B0':'3.0', 'B-':'2.7',
       'C+':'2.3', 'C0':'2.0', 'C-':'1.7',
       'D+':'1.3', 'D0':'1.0', 'D-':'0.7',
       'F':'0.0'}
print(dic[grade])

#문자와 문자열
word = list(input())
num = int(input())
print(word[num-1])

# 그대로 출력하기 - 방법1
while True:
    try:
        print(input())
    except EOFError:
        break

#그대로 출력하기 - 방법2
import sys
s = sys.stdin.readlines()
for i in s:
    print(i.rstrip())


# 그대로 출력하기2 - 방법1
import sys
data = sys.stdin.read()
print(data, end='')

# 그대로 출력하기2 - 방법2
while True:
    try:
        print(input())
    except EOFError:
        break


#문자열 9086번
num = int(input())
for i in range(num):
    string_list = list(input())
    print(string_list[0] + string_list[-1])

# 빠른 A+B
import sys
input = sys.stdin.readline
num = int(input())
for i in range(num):
    a, b = map(int, input().rstrip().split())
    print(a+b)


# 이상한 기호
def cal(x, y):
    return (x+y)*(x-y)

a, b = map(int, input().split())
print(cal(a, b))

#검증수
a, b, c, d, e = map(int, input().split())
print((a*a + b*b + c*c + d*d + e*e) % 10)
