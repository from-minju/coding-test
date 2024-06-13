operator = ['*', '+', '-']

operators = []
numbers = []

def separate_str (str) :

    while True:

        for i in range(len(str)):
            if str[i] in operator:
                operators.append(str[i])
                numbers.append(int(str[:i]))
                str = str[i+1:]
                break
        else:
            numbers.append(int(str))
            break
        

    
    

string = input()
separate_str(string)
print(operators)
print(numbers)