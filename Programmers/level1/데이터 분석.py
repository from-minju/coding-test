'''
1. ext의 값이 val_ext보다 작은 데이터를 뽑아냄
    ext의 인덱스를 알아내야함.
2. sort_by를 기준으로 오름차순 정렬 
'''

def solution(datas, ext, val_ext, sort_by):
    dic = {"code":0, "date":1, "maximum":2, "remain":3}
    ext = dic[ext]
    sort_by = dic[sort_by]
    result = []
    
    result = list(filter(lambda x : x[ext] < val_ext, datas))
    # for data in datas:
    #     if data[ext] < val_ext:
    #         result.append(data)
    
    result.sort(key=lambda x : x[sort_by])
    
    return result