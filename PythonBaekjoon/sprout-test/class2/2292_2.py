n = int(input())

nums, layer = 1, 1
while n > nums:
    nums += 6 * layer
    layer += 1

print(layer)

#https://velog.io/@jieuihong/%EB%B0%B1%EC%A4%80-2292-%EB%B2%8C%EC%A7%91%EB%B8%8C%EB%A1%A0%EC%A6%882-Python