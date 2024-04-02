#==팰린드롬수== 혼자풀은거.
str = 1
while (str != 0):
    
    result = 0
    try: 
        str = input()
        if (str == '0'): break
        else: 
            for i in range(0, len(str)//2):
                if(str[i] != str[-1-i]):
                    result = -1
                    break
        
        if result == -1: 
            print("no") 
        elif result == 0:
            print("yes")
    except EOFError:
        break

    