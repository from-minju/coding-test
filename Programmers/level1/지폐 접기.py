def solution(wallet, bill):
    answer = 0
    
    while not ((wallet[0] >= bill[0] and wallet[1] >= bill[1]) 
               or (wallet[0] >= bill[1] and wallet[1] >= bill[0])):
        answer += 1
        
        if bill[0] >= bill[1]:
            bill[0] = int(bill[0] / 2) #int()말고 //연산자로도 가능. 
        else:
            bill[1] = int(bill[1] / 2)
            
    return answer