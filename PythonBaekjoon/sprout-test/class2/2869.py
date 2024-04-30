# 2869. 달팽이는 올라가고 싶다.

# 나의 코드
a, b, v = map(int, input().split())

if (v-b)%(a-b)==0: print((v-b)//(a-b))
else: print((v-b)//(a-b) + 1)


'''
높이가 V미터
낮 : A미터 위로
밤 : B미터 아래로
단, 정상에 올라가면 미끄러지지 않는다.
-> 정상까지 몇일이 걸리는가?

x일 걸린다 했을 때,
Ax - B(x-1) >= V 를 만족해야함.
'''


# #다른 코드
# a,b,v = map(int,input().split())
# k = (v-b)/(a-b)
# print(int(k) if k == int(k) else int(k)+1)