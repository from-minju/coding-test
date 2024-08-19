# 가운데 글자 가져오기 

def solution(s):
    answer = ''
    length = len(s)
    # 단어길이가 짝수
    if length%2==0:
        answer = s[int(length/2 - 1)] + s[int(length/2)]
    # 단어길이가 홀수
    else:
        answer = s[int(length/2)]
    
    return answer

# 나누기 연산자 /
# print(4/2) -> 2.0
# int형이 아니라 float. 주의!