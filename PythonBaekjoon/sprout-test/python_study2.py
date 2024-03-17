#4장 리스트와 함수

#리스트
a = [10, 20, 30]
print(a)

#len() : 리스트의 요소 개수
#sum() : 리스트에 들어있는 값의 합계

#노래제목을 무작위로 표시하는 프로그램 예제
import random
proverb = [
    "한 페이지가 될 수 있게",
    "Welcome to the Show",
    "Zombie",
    "예뻤어",
    "Sweet Chaos",
    "For me"
]
i = random.randint(0, len(proverb)-1) #random.randint(n.m) : n~m중에서 랜덤한 수
print(proverb[i])


#enumerate()함수 : (인덱스 번호, 요소의 값)의 튜플을 구할 수 있음.
fruits = ["Strawberry", "Apple", "Banana"]
for i,v in enumerate(fruits):
    print(i,v)

print(list(enumerate(fruits)))
#리스트 : []대괄호
#튜플 : ()소괄호


#append() : 리스트에 요소 추가
#리스트명.append() ->이미 만들어진 리스트의 맨 뒤에 값 추가

#append()예제 - 30점 이하의 데이터만을 선택해서 낮은 점수 리스트에 추가하기
points = [90, 100, 32, 44, 11, 10, 20, 23, 30, 67, 88]
least = [] #빈 리스트
for i in points:
    if(i<=30):
        least.append(i)

print(least)

#insert() : 리스트에 요소 추가, 리스트의 중간!에 요소 삽입 가능
#리스트명.insert(삽입위치, 삽입요소)
a = [1, 2, 4, 5]
a.insert(2, 3)
print(a)

#리스트 결합 : +연산자, extend()
#+연산자를 사용한 리스트 결합 -> 원본파괴X, 비파괴적
n1 = [1,3,5]
n2 = [2,4,6]
n3 = n1+n2
print(n3)

#extend()를 이용한 리스트 결합 -> 원본파괴, 파괴적
list_a = [1,2,3]
list_b = [4,5,6]
list_a.extend(list_b)
print("list_a", list_a)
print("list_b", list_b)


#리스트 요소 슬라이스
#리스트[시작인덱스:끝인덱스+1:스텝]
#스탭 : 스탭번째에 등장하는 값
#0번과 마지막 요소는 인덱스 생략할 수 있음. ex) a[:3] == a[0:3]
a = [1, 2, 3, 4, 5, 6]
print(a[1:3]) #result : [2,3]
print(a[::2])
print(a[-4:]) #음수는 마지막에서부터

b = [0,1,2,3,4,5,6,7,8,9]
print(b[2:7:2]) #[2,4,6]
print(b[::3]) #[0,3,6,9]


#리스트 요소 삭제
# -인덱스로 제거 : del키워드, pop()
# -값으로 제거 : remove()
# -모두 제거 : clear()

#인덱스로 제거 -> 모두 원본파괴
# -del 리스트명 [인덱스]
# -리스트명.pop(인덱스)
print("\n<인덱스 제거>")
num = [1,2,3,4,5,6,7,8,9,10]
del num[4]
print(num)
num.insert(4,5)
print("회복", num)

num.pop(4)
print(num)
num.insert(4,5)
print("회복", num)

#값으로 제거 
# -리스트.remove(x) : 리스트 안에 있는 값 x를 삭제
print("\n<값으로 제거>")
num.remove(10)
print(num)

num2 = [1,2,1,3,5,4,5,6,7,8,9,10] # 동일한 값이 여러개있다면, 가장 앞에 위치한 값부터 제거
num2.remove(1) #result: [2,1,3,...10]
print(num2)

#모두 제거 - 리스트.clear()
print("\n<모두 제거>")
num2.clear()
print(num2)
