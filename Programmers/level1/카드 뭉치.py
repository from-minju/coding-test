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
            

        