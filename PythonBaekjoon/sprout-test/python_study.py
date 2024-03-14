#표준 모듈 - datetime
import datetime
print(datetime.date.today()) #2024-03-14

#문자열 반복 연산자 *
print("안녕하세요! "*3)

#문자선택연산자(인덱싱) []
sentence = "초콜릿코스핫아이스"
print(sentence[-4], sentence[0], sentence[3]) #핫 초 코
print(sentence[-4]+sentence[0]+sentence[3]) #핫초코

#문자열범위선택연산자(슬라이싱) [a:b] ->[a]부터 [b-1]까지 출력됨. 
print(sentence[-3:]+sentence[:3]) #아이스초콜릿
print(sentence[3:5]) #코스

#문자열의 길이를 알아내는 함수 len()
print(len(sentence))

#input
name = input("お名前は？") #사용자로부터 입력을 요구할때의 멘트를 같이 쓸 수 있음.
print("こんにちは"+name+"さん")
print(type(name)) #input함수는 무조건 str형태로 받아옴. 숫자도 str으로 받음.


height = input("당신의 키를 인치로 바꿔드립니다.\n당신의 키는 몇cm입니까? ->")
inch = int(height)/2.54
print(type(inch)) #float

inch = float(height)/2.54
print("-->당신의 키는 {0}inch입니다.\n({cm}cm = {inch}inch)"
      .format(round(inch,2), cm=height, inch=inch))

#수치와 문자열을 변환하는 함수
#연산할때 형을 반드시 맞춰야 함. ->숫자와 숫자, 문자와 문자
print(str(height))
# print(type( str(10) ))
print(float(10))
print(int(3.5))