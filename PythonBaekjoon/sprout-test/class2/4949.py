#4949. 균형잡힌 세상

while True:
    stack = []
    result = "yes"

    str = input()

    if str == '.': break
    else:

        for i in str:
            if i=='(' or i=='[':
                stack.append(i)
            elif i==')' or i==']':
                if stack: #스택이 비어있지 않으면
                    temp = stack.pop()

                    if temp=='(': temp=')'
                    elif temp=='[': temp=']'

                    if i == temp:
                        continue
                    else:
                        result = "no"
                        break
                else: #(().와 같은 상황
                    result = "no"
                    break

        if stack: #스택이 비어있지 않으면
            result = "no"
            
        print(result)