# 실전문제: 왕실의 나이트 - 내 답

input_data = input()
column = ord(input_data[0]) - 96 #알파벳으로 받음. 
row = int(input_data[1])

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