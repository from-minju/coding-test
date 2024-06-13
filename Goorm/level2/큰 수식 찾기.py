

# 연산자와 숫자로 나눠주는 함수
def str_to_list (str) :
    formula = []

    while True:
        for i in range(len(str)):
            if str[i] in ['*', '+', '-']:
                formula.append(int(str[:i]))
                formula.append(str[i])
                str = str[i+1:]
                break
        else:
            formula.append(int(str))
            break
    
    return formula

# 계산한값을 리턴하는 함수
def calculate (formula):
    # * 계산
    while True:
        for i in range(len(formula)):
            if formula[i] == '*':
                temp = formula[i-1] * formula[i+1]
                formula = formula[:i-1] + [temp] + formula[i+2:]
                break
        else:
            break
    
    # +, - 계산
    while True:
        for i in range(len(formula)):
            if formula[i] in ['+', '-']:
                if formula[i] == '+':
                    temp = formula[i-1] + formula[i+1]
                elif formula[i] == '-':
                    temp = formula[i-1] - formula[i+1]
                formula = formula[:i-1] + [temp] + formula[i+2:]
                break
        else:
            break
    
    return formula[0]
    


A, B = input().split()
A = calculate(str_to_list(A))
B = calculate(str_to_list(B))

if A > B:
    print(A)
else:
    print(B)
