def solution(name, yearning, photos):
    answer = []
    dic = {}
    
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    
    for photo in photos:
        sum = 0
        for person in photo:
            if person in dic:
                sum += dic[person]
        answer.append(sum)
    return answer