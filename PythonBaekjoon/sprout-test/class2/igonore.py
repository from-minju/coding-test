# list = [1,2,3,4,5] 
# list.reverse()
# print(list) #[5, 4, 3, 2, 1]
# print(type(list)) #<class 'list'>

origin_list = [1,2,3,4,5]
reversed_list = reversed(origin_list)
print(reversed_list)
print(type(reversed_list))

reversed_list = list(reversed_list)
print(reversed_list)
print(type(reversed_list))

