
def makeDoubleDigit(x):
    x = int(x)
    if x < 10:
        x = "0" + str(x)
    return str(x)

def solution(today, terms, privacies):
    result = []
    
    # terms -> 딕셔너리로 변환 
    termsDic = {}
    for term in terms:
        a, b = term.split(" ")
        termsDic[a] = int(b)
    
    today = "".join(today.split("."))
    
    for idx, privacy in enumerate(privacies):
        date, term = privacy.split(" ")
        term = termsDic[term]
        y, m, d = map(int, date.split("."))
        
        # 파기일 계산
        m += term
        if m > 12:
            y += m // 12
            m = m % 12
            if m==0: 
                m = 12
                y -= 1
        
        date = "".join(map(makeDoubleDigit, [y, m, d]))

        if (int(today) >= int(date)):
            result.append(idx+1)
    
    return result

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C", "2021.05.20 B"]
print(solution(today, terms, privacies))