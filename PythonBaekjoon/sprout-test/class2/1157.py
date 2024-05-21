# 단어공부

count_list = [0] * 26

word = input()
word = word.upper()

for w in word:
    count_list[ord(w) - 65] += 1

max = max(count_list)
if count_list.count(max) >= 2:
    print('?')
else :
    print(chr(count_list.index(max) + 65))


    