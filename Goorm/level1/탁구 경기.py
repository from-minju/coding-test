n = int(input())

winners = [input() for _ in range(n)]
d = 0
p = 0

for i in winners:
	if i == 'D':
		d+=1
	else:
		p+=1
	
	if abs(d-p)>=2:
		break

print(str(d) + ":" + str(p))