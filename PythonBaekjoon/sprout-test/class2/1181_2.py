#==단어정렬==

words = list(set( input() for i in range(int(input())))) #중복 단어를 제거한 단어 리스트
words.sort() #단어를 오름차순으로 정렬
words.sort(key=len)
for _ in words: print(_)

