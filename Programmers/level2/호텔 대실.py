def convertTime(time):
    h, m = map(int, time.split(':'))
    
    return h*60 + m 
    
    
def solution(book_time):
    room = []
    
    book_time.sort(key = lambda x : convertTime(x[0]))
    
    room.append(convertTime(book_time[0][1]) + 10)
    
    for time in book_time[1:]:
        start = convertTime(time[0])
        end = convertTime(time[1])
        
        for idx, t in enumerate(room):
            if start >= t:
                room[idx] = end + 10
                break
        else:
            room.append(end + 10)
    
    return len(room)
            
            
    