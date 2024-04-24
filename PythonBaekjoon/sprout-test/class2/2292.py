# 벌집

n = int(input())

if n==1:
    ans = 1
else:

    mul = 1
    start = 2

    while True:
        end = start + mul*6

        if start <= n < end:
            ans = mul + 1
            break
            
        start = end
        mul += 1
    
        

print(ans)

'''
1 -1
2 3 4 5 6 7 -6
8 9 10 11 12 13 14 15 16 17 18 19 -12
20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 - 18
- 24


'''
