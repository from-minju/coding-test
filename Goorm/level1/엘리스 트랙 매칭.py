from collections import Counter

n = int(input())
friends_data = list(input().split())
my_data = input()

friends_data = Counter(friends_data)

print(friends_data[my_data])
