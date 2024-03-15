#문제 10699번 - 오늘 날짜 출력하기
import datetime
print(datetime.date.today())

#A+B
#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
int1, int2 = input().split()
print(int(int1)+int(int2))

#사칙연산
#두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.
#파이썬3의 나누기 연산은 기본적으로 실수 출력이 되기 때문에 int형으로 변환함.
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)

#꼬마정민 - A+B+C계산
a, b, c = map(int, input().split())
print(a+b+c)

#두 수 비교하기
a, b = map(int, input().split())
if(a>b):
    print(">")
elif(a<b):
    print("<")
else:
    print("==")

#시험성적
#시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력
a = int(input())
if(90<=a<=100):
    print("A")
elif(80<=a<=89):
    print("B")
elif(70<=a<=79):
    print("C")
elif(60<=a<=69):
    print("D")
else:
    print("F")

#사분면 고르기
x = int(input())
y = int(input())

if(x>=0 and y>=0):
    print(1)
elif(x<0 and y>=0):
    print(2)
elif(x<0 and y<0):
    print(3)
else:
    print(4)