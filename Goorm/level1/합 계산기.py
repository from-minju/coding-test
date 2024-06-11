t = int(input())

result = 0

for _ in range(t):
	inputs = list(input().split())
	
	if inputs[1] == '+':
		result += int(inputs[0]) + int(inputs[2])
	elif inputs[1] == '-':
		result += int(inputs[0]) - int(inputs[2])
	elif inputs[1] == '*':
		result += int(inputs[0]) * int(inputs[2])
	elif inputs[1] == '/':
		result += int(inputs[0]) // int(inputs[2])
	
print(result)
	