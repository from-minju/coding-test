arr = [[1,3,2,0], [2,0,1,3], [1,2,0,3]]

n = len(arr[0])
k = len(arr)

result = []

for i in range(n):
    value = 0
    for j in range(k-1):
        idx1 = arr[j].index(i)
        idx2 = arr[j+1].index(i)
        value += abs(idx1 - idx2)
    result.append(value)
print(result)