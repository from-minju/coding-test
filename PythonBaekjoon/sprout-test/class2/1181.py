#==단어정렬==

num = int(input())
words_dict = {} #입력받은 단어들의 딕셔너리 (단어, 단어길이수)
sorted_keys_list = []

for i in range(num): #딕셔너리로 input받음.
    temp = input()
    words_dict[temp] = len(temp)

values_list = list(set(words_dict.values()))
values_list.sort()

for wd_len in values_list: #길이수 오름차순으로 단어 출력
    search_result = [k for k,v in words_dict.items() if v == wd_len] #길이수에 해당하는 키값을 리스트로 받아옴.
    if(len(search_result) != 1): #단어수가 같은 경우가 있을 때
        search_result.sort() #오름차순으로 정렬. (사전순으로)
        for i in search_result:
            sorted_keys_list.append(i)

    else: #길이수에 해당하는 단어가 하나라면
        sorted_keys_list.append(search_result[0])


#최종결과출력
for word in sorted_keys_list:
    print(word)
