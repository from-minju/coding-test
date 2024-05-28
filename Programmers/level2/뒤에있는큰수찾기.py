# 뒤에있는큰수찾기 

def solution(numbers):
    answer = [-1]*len(numbers)

    stack = []

    for index in range(len(numbers)):
        target = numbers[index]
        while stack and numbers[stack[-1]]<target:
            answer[stack.pop()]=target
        stack.append(index)
    
    return answer

inputs = list(map(int, input().split()))
print(solution(inputs))