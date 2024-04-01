#4장 리스트와 함수

#-----------------------------------
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

#리스트 - 자주 사용되는 메소드
#index(x) : 값x의 위치(인덱스)를 리턴함. a=[1,2,3], a.index(1) => 0
#count(x) : 리스트에서 값 x가 몇 개 있는지 센다. a.count(1) => 1
#sort(key, reverse) : 리스트를 오름차순으로 다시 정렬한다. reverse=True이면 내림차순.
#copy() : 리스트를 복사해서 리턴. (얕은 복사)


#-----------------------------------
# :: 튜플 tuple ::
#튜플은 요소의 값을 변경할 수 없음!!
print("\n\n  :: 튜플 ::")
a = (10, 20, 30)
print(type(a))
print(a[:2]) #[0]~[1]까지


#튜플과 리스트는 서로 변환 가능
# - 튜플 -> 리스트 : list()
# - 리스트 -> 튜플 : tuple()
list_ex = [1,2,3,4]
tuple_ex = (5,6,7,8)

print(type(tuple(list_ex))) #리스트->튜플
print(list(tuple_ex)) #튜플->리스트
print(tuple(list_ex))
print(list_ex) #list(), tuple() - 비파괴적임.


#-----------------------------------
#  :: 집합 set {} ::
# 중복되는 값 불가능!! 순서를 매길 수도 없음!!
# 집합 생성하는 법 : {}중괄호, set()함수
# 대신 집합으로 수학적 연산(결합,교차,차집합)가능
# 빈 집합 생성: set()을 통해서만. 그냥 {}만 써놓은건 빈 딕셔너리를 의미
# 원소 추가 : set.add(값)
#{'strawberry', 'melon', 'lemon'}
print("\n\n  :: 집합 ::")
colors = {"red", "green", "blue"}
print(colors)
e = set() #빈 집합 만들기
print(e)

fruits = set({"strawberry", "melon", "lemon"})
print(fruits)
print(type(fruits))

#차집합 계산 : - 연산자
bag1 = {'keyring', 'card', 'album', 'ticket'}
bag2 = {'album', 'keyring'}
print(bag1-bag2)

# 요소 in 집합 : 어떤 요소가 집합에 포함되어 있는지 조사할 수 있음. -> 리턴값 : True/False
print('album' in bag1) #True
print('band' in bag2) #False

# | 연산자 : 여러개의 집합을 하나로 통합할 때. (+연산자 아님 주의!), 중복값 허용X
bag3 = bag1 | bag2
print(bag3)

# & 연산자 : 두 집합에 공통으로 포함된 값
bag4 = bag1 & bag2
print(bag4)



#-----------------------------------
# :: 딕셔너리 dict {} ::
#python3.6부터는 딕셔너리의 순서보존함. 이전에는 원래는 순서보장안함.
#{'김원필': 94, '강영현': '93', '박성진': 93, '윤도운': 95, '마이데이': 24}
#빈 딕셔너리 만들기 : {}
print("\n\n  :: 딕셔너리 ::")
day6 = {'김원필':94, '강영현':'93', '박성진':93, '윤도운':95, '마이데이':24}
print(day6)
print(type(day6))
print(day6['김원필'])
day6['마이데이'] = '00' #값에 int랑 string이랑 같이 저장가능한듯
print(day6['마이데이'])

# in : 딕셔너리에 키가 포함되어 있는지 확인하는 방법 ->리턴값 : True/False
print("마이데이" in day6) #True

# keys() : 키key 목록을 열거
#순서보장하지 않음. 알파벳순서로 정렬하고싶으면 sorted()이용. but, 영문 숫자이외의 문자 정렬할때는 주의. sorted()는 데이터를 문자 코드 순서로 정렬할 뿐임.
#딕셔너리.keys() -> dict_keys형으로 리턴됨.
#dict_keys형 -> list형으로 변환 : list(딕셔너리.keys())
print(day6.keys()) #dict_keys(['김원필', '강영현', '박성진', '윤도운', '마이데이'])
print(type(day6.keys())) #dict_keys
print(list(day6.keys()))
print(type(list(day6.keys()))) #list

print(sorted(day6.keys()))#딕셔너리 키목록을 오름차순으로 정렬


#딕셔너리형을 열거하는 방법
# - list(d.keys()) :키 목록을 리스트형으로
# - sorted(d.keys()) : 키 목록을 정렬된 리스트형으로
# - d.values() : 값 목록
# - list(d.items()) : (키,값)으로 조합된 튜플형태의 리스트로 목록을 얻음.
print(list(day6.items()))


#딕셔너리를 for문과 함께 사용하는 예제1
for member in day6.keys():
    print(" * {0} ({1})".format(member, day6[member]))

#딕셔너리를 for문과 함께 사용하는 예제2
# for 키,값 in 딕셔너리.items()
for name, birth in day6.items():
    print(" -{0}({1})".format(name, birth))

#[예제] 영어 단어가 출현하는 횟수를 세어보자.
print("\n[예제] 중복된 영어 단어를 출력합니다.")
text = """
Keep on asking, and it will be given you;
keep on seeking, and yo will find;
keep on knocking, and it will be opened to you;
for everyone asking receives, and everyone seeking finds,
and to everyone knocking, it will be opened.
"""

text = text.replace(";","") #텍스트 대치 - 단어를 구분하기 위한.
text = text.replace(",","")
text = text.replace(".","")

words = text.split() #공백으로 텍스트를 나눈다. list형태로.

counter = {} #빈 딕셔너리
for w in words:
    ws = w.lower()#소문자로 변환
    if ws in counter:
        counter[ws] += 1
    else:
        counter[ws] = 1

for k,v in sorted(counter.items()):
    if v >= 3:
        print(k, ":", v)
 

print("\n\n :: 문자열을 다루는 메서드 ::")
#-----------------------------------
# :: 문자열을 다루는 메서드 ::
# - str.find(검색키워드, 탐색할문자열시작위치, 끝위치)
# - split() : 문자열 분할 / 문자열.split(구분문자)
# - replace() : 문자열 치환 / 비파괴적 / 문자열.replace("검색단어", "치환 후의 내용")
# - str.lower(), upper() : 소문자, 대문자로 변환/ 비파괴적
# - str.join() : 구분자.join(리스트 등) /
a = ["안녕", "하세요"]
print(", ".join(a)) #안녕, 하세요

# - str.strip() : 문자열 및 공백 제거
text = "##Hello, World!##"
print(text.strip("#"))  
ex_strip = "파          파   이 썬        연    습"
print(ex_strip.strip()) #왜 공백이 제거가 안되지...?원래 돼야하는건데..?!

# - str.startswith(), endswith() -> 리턴값 : True/False
# str.startswith(시작하는문자, 시작지점) / str.endswith(끝나는문자, 시작지점, 끝지점)
str = 'Hello world, Python!'
if str.startswith('Hello'):
    print('It starts with Hello')
if not str.startswith('Python'):
    print('It does not start with Python')

# - str.isnumeric() : 문자열 전체가 숫자값으로 구성돼 있다면 True 반환
#True반환하는 값 : 제곱근, 분수, 거듭제곱 형태의 특수문자
#False반환하는 값 : 음수, float형
number = ['123', '-1', '0.5', '½', '3²', '50%']
print(" [예제] str.isnumeric()")
for i in number:
    print(i, ":", i.isnumeric())

#-----------------------------------
# :: 정렬 메서드 ::
# - list.sort() : [파괴적] 리스트 자체를 정렬시킴
# - sorted(list) : [비파괴적] 새로 정렬된 리스트를 반환
#새로운 정렬된 리스트를 반환하는 함수는 sorted 함수이고, 리스트 자체를 정렬시켜버리는 것은 sort 함수입니다.