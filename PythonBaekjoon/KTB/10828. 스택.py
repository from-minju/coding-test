import sys
input = sys.stdin.readline
n = int(input().strip())

stack = []

for _ in range(n):
    order = input().strip()

    if ' ' in order:
        o, num = order.split(" ")
        num = int(num)
        stack.append(num)
    elif order == "pop":
        if len(stack) <= 0:
            print("-1")
        else:
            print(stack[-1])
            stack.pop()
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif order == "top":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print("-1")

        




# n = int(input())
# stack = []

# for i in range(n):
#     order = input()

#     if ' ' in order:
#         o, num = order.split(" ")
#         num = int(num)
#         stack.append(num)
#     elif order == "pop":
#         if len(stack) <= 0:
#             print("-1")
#         else:
#             print(stack[-1])
#             stack.pop()
#     elif order == "size":
#         print(len(stack))
#     elif order == "empty":
#         if len(stack) > 0:
#             print(0)
#         else:
#             print(1)
#     elif order == "top":
#         if len(stack) > 0:
#             print(stack[-1])
#         else:
#             print("-1")

        

