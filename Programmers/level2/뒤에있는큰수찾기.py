# 뒤에있는큰수찾기 

def solution(numbers):
    # 뒷큰수를 담을 리스트
    answer = [-1]*len(numbers) #-1로 초기화 

    # 뒷큰수를 아직 만나지 못한 수들을 담는 리스트
    stack = [] 

    # target이 스택에 담긴 수들의 뒷큰수가 될 수 있는지 확인
    for idx, target in enumerate(numbers):
        while stack and numbers[stack[-1]]<target:
            answer[stack.pop()] = target
        stack.append(idx)
    
    return answer

inputs = list(map(int, input().split()))
print(solution(inputs))

#stack에서 pop꺼내지 않고 원소를 가져오기만 할때는 stack[-1]를 사용
