import sys
while 1:
    n = sys.stdin.readline()[:-1]
    if n == '0': break

    if n == n[::-1]:
        print('yes')
    else:
        print('no')