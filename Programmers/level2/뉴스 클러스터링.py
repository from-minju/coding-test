from collections import Counter

def solution(str1, str2):

    def getList(str):
        result = []
        
        for i in range(len(str) - 1):
            temp = str[i:i+2]
            if temp.isalpha():
                result.append(temp.lower())
        
        return result
        

    
    # 리스트 만들기
    list1 = getList(str1)
    list2 = getList(str2)
    print(list1, list2)

    # 교집합 크기 구하기
    and_size = 0
    and_counter = Counter(list1) & Counter(list2)
    for k in and_counter:
        and_size += and_counter[k]
    
    # 합집합 크기
    or_size = len(list1) + len(list2) - and_size

    # 자카드유사도 구하기
    if or_size <= 0: j = 1
    else:
        j = and_size / or_size

    return int(j*65536)

        
    
    
        