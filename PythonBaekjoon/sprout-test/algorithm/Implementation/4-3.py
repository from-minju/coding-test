# 실전문제: 왕실의 나이트

input_data = input()
# column = ord(input_data[0]) - 96 #내 답
column = int(ord(input_data[0]) - int(ord('a'))) + 1 #책 답안 예시
row = int(input_data[1])

#가능한 이동경로
steps = [(-2,-1), (-2,1), (2,-1), (2,1), (-1,-2), (-1,2), (1,-2), (1,2)]

result = 0 

for step in steps:
    next_column = column + step[0]
    next_row = row + step[1]

    if next_column>=1 and next_row<=8 and next_row>=1 and next_row<=8 :
        result += 1

print(result)


'''
알파벳으로 받은 x좌표 -> 유니코드로 변환해서...
'''