#==1259. 팰린드롬수== 더 빠른 버전
import sys
while 1:
    n = sys.stdin.readline()[:-1]
    if n == '0': break

    if n == n[::-1]:
        print('yes')
    else:
        print('no')