# [지역변수와 전역변수]
#class1 - 음계 문제 참고
# 파이썬에서 if문 안에서 처음 선언/설정한 변수는 전역변수임. 
# 다만, 함수 안에서 처음 선언된 변수는 지역변수!! 전역변수로 쓰고 싶다면 global 선언을 해줘야 한다.
# 파이썬은 block scope가 따로 없어서 If를 써도 scope구분이 없다. 즉 아래 3줄코드 모두 같은 scope이다.
if True:
    a = 1000
print(a)


# [유니코드]
# ord() : 어떤 문자의 유니코드 값을 알고싶을 때
# chr() : 어떤 유니코드 값에 해당하는 문자를 알고싶을 때
print( ord('A')) #65
print( ord('a')) #97
print( ord('b')) #98
print( ord('z')) #122

print( chr(98)) #b


# [find(), index()의 차이점]
# 변수.find(찾을문자) ->문자열만!사용 가능 / 리스트,튜플,딕셔너리에서는 안됨!
# 변수.index(찾을문자) ->문자열,리스트,튜플에서 사용 가능 / 딕셔너리에서는 안됨!
# 공통점 : 문자x가 처음! 위치한 자리의 값을 리턴
# 차이점 : 찾는값이 없을 경우 find()는 -1을 반환, 반면, index()는 에러발생.
s1 = '1-1-111--'
print(s1.find('-')) #1
print(s1.index('-')) #1
#시작점과 종료점을 지정 가능.
print(s1.index('-', 3)) #3번째 위치부터 문자'-'가 처음 위치한 자리는?->3
print(s1.find('-', 4, 6)) #-1 : 찾는 값이 없는 경우 -1반환.
#print(s1.index('-', 4, 6)) #Error : ValueError: substring not found

#in , not in ->리턴값: True/False
text = "안녕, 내 이름은 미키야"
result = "미키" in text
print(result) #True


#list의 요소를 Int로 변환
#list_a = ['1', '2', '3', '4']   -> list_a = [1, 2, 3, 4] 로 바꾸고 싶을 때,
list_a = ['1', '2', '3', '4']
list_a = list(map(int, list_a))
print(list_a)


#list가 비어있는지(empty)확인하는 법
list_empty = []
if not list_empty: #list_empty가 비어있는 경우
    print("list_empty는 비어있습니다.")


#list의 모든 요소를 더하기. : sum(list)
i = [1, 2, 3, 4, 5]
print(sum(i))


#어떤 정수m의 각 자릿수의 합 구하기
m = 123
mlist = list(map(int, str(m)))
print(sum(mlist)) #1+2+3=6


#어떤 수의 제곱
# num ** 2 : num의 제곱
num = 5
print(num ** 2) #25


#정수를 리스트로 바꾸기
num = 232443
line = list(map(int,str(num)))
print(line) # 	[2, 3, 2, 4, 4, 3] 요소가 정수임.

x = 12345
list = list(str(x))
print(list) #['1', '2', '3', '4', '5'] 요소가 문자열임.


#팩토리얼
import math
print(math.factorial(3))


# m행 n열의 2차원 리스트
data = [[0]*n for _ in range(m)]
#잘못된 방법
list = [[0]*4]*3
list[1][1] = 1
print(list)


# 큐 deque
from collections import deque
# 비어있는 큐 만들기
deque = deque()
# 원소가 있는 큐 만들기
deque = deque([1, 2, 3])
# 큐 최대 길이 명시하기(원소를 maxlen보다 더 많이 넣으면 maxlen이 자동 갱신됨)
deque = deque(maxlen=5)


#DFS 재귀깊이제한
import sys
sys.setrecursionlimit(10000)


# 문자열 대문자, 소문자
# 대문자로 : string.upper() - 반환함. 원본파괴 X
# 소문자로 : string.lower() - 반환함. 원본파괴 X
# 대문자인가? : string.isupper()
# 소문자인가? : string.islower()
