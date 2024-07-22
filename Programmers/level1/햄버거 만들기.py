'''
리턴: 포장가능한 햄버거 개수
순서: 빵-야채-고기-빵 (1-2-3-1)
'''

# 실패 - 시간초과
def solution(ingredient):
    answer = 0

    stack = []
    for n in ingredient:
        stack.append(n)
        if len(stack) >=4 and stack[-4:] == [1, 2, 3, 1]:
            stack = stack[:-4]
            answer += 1

    return answer

# 성공 
def solution2(ingredient):
    answer = 0

    stack = []
    for n in ingredient:
        stack.append(n)
        if len(stack) >=4 and stack[-4:] == [1, 2, 3, 1]:
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()

            answer += 1

    return answer

# 코드 개선
def solution2(ingredient):
    answer = 0

    stack = []
    for n in ingredient:
        stack.append(n)
        if stack[-4:] == [1, 2, 3, 1]:
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()

            answer += 1

    return answer