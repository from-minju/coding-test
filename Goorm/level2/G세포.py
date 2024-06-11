import math

n = int(input())

times = []

while n>0:
	time = int(math.log2(n))
	times.append(time)
	n -= 2**time

times.sort()

print(len(times))
for i in times:
	print(i, end=" ")

