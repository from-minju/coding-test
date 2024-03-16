
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

#방법1 : 논리연산자
if (year%4==0 and year%100!=0) or year%400==0:
    result = True
else:
    result = False

#방법2 : 중첩if문
if year%4==0:
    if year%100==0:
        result = False
        if year%400==0:
            result = True
else:
    result = False

#방법3 : elif문
if year%400==0:
    result=true
elif year%100==0:
    result=False
elif year%4==0:
    result=True
else:
    result=False

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
for x in range(10): #range(10)의 범위 : 0~9
    print(x, end=" ")
    x+=1
print()
for x in range(1,5): #range(0,5)의 범위 : 1~4
    print(x, end=" ")
    x+=1
print()
for x in range(0,10,2): #range(0,10,2)의 범위 : 0~9까지 2만큼의 차이를 갖음.->0,2,4,6,8
    print(x, end=" ")
    x+=1
print()

#범위 반복을 위한 for문 예제2
sum = 0
for x in range(1,11):
    sum += x
    print("{0}을(를) 더하면 {1}".format(x, sum))
print("1에서 10까지 모두 더하면..." + str(sum))
print("1에서 10까지 모두 더하면...", sum) # +연산자로는 str + int가 불가능 / 하지만 print(str, int)는 가능. 띄어쓰기로 연결됨.

#반복을 중지하는 break와 continue
#FizzBuzz
for x in range(1,21):
    if(x%3==0) and (x%5==0):
        print("FizzBuzz")
        continue #근데 continue안써도 똑같긴함.
    elif(x%3==0):
        print("Fizz")
    elif(x%5==0):
        print("Buzz")
    else:
        print(x)


#반복문에서 else블록을 사용할 경우
#1. 반복문을 한 번도 실행하지 않았을 때.
i=8
while i<5: #조건이 거짓이라 반복문 실행 안함.
    print("...")
else:
    print("반복문을 한 번도 실행하지 않았습니다.", i)

#반복문을 모두 끝냈을때(단, break로 반복문을 빠져나오지 않았을 때만. braek문 만나면 else거치지 않고 바로 반복문 밖으로 빠져나감.)
i=3
while i<5:
    print(i)
    if i ==2 : break
    i += 1
else:
    print("반복문을 모두 실행하였습니다.", i)
print("반복문을 빠져나왔습니다.")

#반복문에서 else 블록을 사용할 경우 예제2
foodstuff = ["Banana", "Chocolate", "Mango", "Strawberry", "Melon"]
for food in foodstuff:
    if food == "Strawberry":
        print("냉장고 안에 딸기가 있습니다!")
        break
else: #if문이 수행되지 않았을 경우 (if문이 수행되면 break문을 만나 밖으로 빠져나가기 때문.)
    print("딸기가 없어요ㅠㅠ")