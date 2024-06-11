n = int(input())

datas = [tuple(input().split()) for _ in range(n)]

have = 0
spent = 0

for c,v in datas:
	v = int(v)
	
	if c == 'in':
		have += v 
	elif c == 'out':
		spent += v 
	
	if spent > have :
		print('fail')
		break
else:
	print('success')
