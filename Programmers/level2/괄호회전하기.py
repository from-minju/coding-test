# 괄호 회전하기

# 바른 문자열인지 확인하는 함수
def is_correct(s):
    stack = []
    left = ["[", "(", "{"] # 왼쪽 괄호
    right = ["]", ")", "}"] # 오른쪽 괄호
    
    for str in s:
        # str이 [ ( { 인 경우 -> 스택에 넣음
        if str in left:
            stack.append(str)
        # str이 ] ) } 인 경우 -> pop()한거랑 짝이 맞는지 확인
        else: 
            # 스택이 비어있지 않고 pop()한것과 str의 짝이 맞다면 계속
            if stack and str == right[left.index(stack.pop())]: continue
            else: break
    #모두 짝이 맞는 경우
    else:
        # 스택이 비어있다면 바른 문자열, 스택이 비어있지않다면 올바르지 못한 문자열
        if not stack: 
            return True
    
    return False
            
            

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        if is_correct(s): # 바른 문자열인 경우
            answer += 1
        # 문자열 왼쪽으로 이동
        s = s[1:] + s[0]
    return answer