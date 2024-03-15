
#if문 예제
tp = int(input("오늘의 온도는? : "))
if tp>20:
    print("따뜻하네용!")
else:
    print("추워요ㅜ")

#bool타입
if None: #False로 변환되는 값 : None, 0, 0.0, 빈 컨테이너
    print("False")
else:
    print("True")

#논리연산자 : and, or, not
num1 = 15
if(10<= num1 <=20): #python3에서는 두개의 비교식을 and로 조합하는방법 외에 이렇게도 가능
    print(str(num1)+"은(는) 10이상 20이하입니다.")

#if문예제 - 윤년을 판정하는 프로그램
#윤년의 조건 : 
#   1. 기본적으로 연도 수가 4로 나누어 떨어지면 윤년
#   2. 그러나 100으로 나누어 떨어지는 해는 윤년이 아님. ->100으로 나누어 떨어지지 않으면 윤년
#   3. 그러나 400으로 나누어 떨어지는 해는 윤년

year = int(input("서기 몇 년? : "))
result = True

#방법1
if (year%4==0 and year%100!=0) or year%400==0:
    result = True
else:
    result = False

##방법2
if year%4==0:
    if year%100==0:
        result = False
        if year%400==0:
            result = True
else:
    result = False

#결과 출력
if result==True:
    print("윤년입니다.")
else:
    print("윤년이 아닙니다.")


#pass문
n = 3
if n==3:
    pass #어떤 처리도 실행하지 않고 넘어감. 
else:
    print(n)

#단문의 if구문 - else문이 없을 경우에만 가능.
if n%3==0:print(n)


#while문
#Ctrl + C :파이썬 프로그램을 강제로 끝내는 방법(무한루프에서 빠져나올때도 사용가능)
#break문으로 무한루프 빠져나올 수 있음.
while n>1:
    print("while true")
    n=n-1
else:
    print("while false")


#범위 반복을 위한 for문


