N = int(input())
vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for _ in range(N):
	sentence = list(input())
	
	have_vowel = list(set(sentence) & set(vowel))
	if not have_vowel:
		print("???")
		continue
	
	for c in sentence:
		if c in vowel:
			print(c, end ='')
	print()
			

