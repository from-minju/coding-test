from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    
    pop1 = cards1.popleft()
    pop2 = cards2.popleft()
    
    for card in goal:
        if pop1 == card:
            if cards1: pop1 = cards1.popleft()

        elif pop2 == card:
            if cards2: pop2 = cards2.popleft()
            
        else:
            return "No"
        
    return "Yes"
            

def solution1(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)

    for card in goal:
        if cards1 and cards1[0] == card:
            cards1.popleft()

        elif cards2 and cards2[0] == card:
            cards2.popleft()
            
        else:
            return "No"
        
    return "Yes"


def solution2(cards1, cards2, goal):
    for card in goal:
        if len(cards1) > 0 and card == cards1[0]:
            cards1.pop(0)       
        elif len(cards2) >0 and card == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"
            

def solution3(cards1, cards2, goal):
    idx1,idx2=0,0
    for word in goal:
        if len(cards1)>idx1 and cards1[idx1]==word:
            idx1+=1
        elif len(cards2)>idx2 and cards2[idx2]==word:
            idx2+=1
        else:
            return "No"
    return "Yes"
        