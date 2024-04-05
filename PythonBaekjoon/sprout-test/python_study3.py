# #4장 리스트와 함수

# #-----------------------------------
# #함수
# def sum(a,b):
#     return a+b

# #docstring : 함수에 설명문을 추가하는 기능
# def mul(a,b):
#     '''곱셈하는 함수'''
#     return a*b
# #help(mul) #'곱셈하는 함수'라고 알려줌.


# #재귀함수
# #재귀함수 예제 - 계승을 구한다. 팩토리얼
# def fact(n):
#     if n==0: #인수가 0이면 1을 반환한다
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(3))

# #함수 인수의 기본값(초깃값) - 해당 인수가 지정되지 않은 상황에서 함수를 호출하면 기본값이 사용됨.
# def print_basic(member="마이데이"):
#     if member=="김원필":
#         return "건반"
#     elif member=="강영현":
#         return "베이스"
#     elif member=="마이데이":
#         return "팬"

# print(print_basic()) # 인수를 지정하지 않았으므로 기본값으로 설정한 '마이데이'로 값을 인식->리턴값: 팬


# #키워드 인수 : 인수의 이름을 지정해서 함수를 호출할 수 있음.
# def keyword(dist, speed):
#     print(dist)
#     print(speed)

# keyword(speed=50, dist=100)


# #가변 개수 인수 : 개수가 변하는 인수
# #변수명 앞에 *기호를 추가해주면 가변개수인수가 됨.
# #가변개수인수에 튜플 형식으로 대입됨.
# def sumArgs (*args):
#     print(args)
# sumArgs(1,2,3)
# sumArgs(4,5)

# #딕셔너리형 가변 개수 인수
# # **를 변수명 앞에 추가하면 됨.
# def print_args(**x):
#     print(x)
#     print(type(x))
# print_args(a=30, b=50)
# print_args(aa="hello")

# #가변개수인수 정리
# # *args : 튜플
# # **args : 딕셔너리
# def sumArgs(*args):
#     v = 0
#     for n in args:
#         v += n
#     return n
# print(sumArgs(1,2,3)) #*args는 튜플형식으로 값을 넣음. 
# print(sumArgs(1,2,3,4,5,6))

# def print_args(**args): #**args는 딕셔너리형으로 
#     print(args)
#     print(type(args)) #<class 'dict'>
# print_args(a=30, b=40)
# print_args(aa="coffee", bb="tea")

# #-----------------------------------
# #==지역변수와 전역변수==
# #지역변수 : 변수명이 같더라도 함수 안과 함수 밖에서 사용하는 변수는 다름. 
# #전역변수 : 함수 안에서 다시 global로 선언해주면 함수 안과밖에있는 변수 일치시킬 수 있음. 

# #전역변수 예시
# value = 100
# def changeValue():
#     global value #global로 선언하면 전역변수
#     value = 20
# changeValue()
# print("value = ", value)

# #-함수명을 변수에 대입할 수 있음.
# #-함수명()을 대입하면 함수의 결과값을 대입하는거임.
# #-함수를 인수로 받는 함수를 정의할 수 있음.


# #-----------------------------------
# #==익명 함수==




