def solution (N, Arr):
    #Character 선언
    Character = {
        '마블' : ['아이언맨', '토르', '헐크', '블랙위도우', '캡틴아메리카', '캡틴마블', '호크아이', '그루트', '비전', '스칼렛위치'],
        '짱구' : ['신짱구', '신짱아', '봉미선', '흰둥이', '신영식', '김철수', '한유리', '맹구', '한수지', '채성아'],
        '둘리' : ['둘리', '도우너', '또치', '마이클', '고길동', '김박사', '매머드', '램프노인', '공실이'],
        '뽀로로' : ['뽀로로', '크롱', '에디', '로디', '루피', '패티', '포비', '해리', '뽀뽀', '퉁퉁이']
    }

    genre = ['마블', '짱구', '둘리', '뽀로로']

    counting = {'마블':0, '짱구':0, '둘리':0, '뽀로로':0, '미분류':0}

    # 장르의 수 카운팅해주기
    for char in Arr:
        for g in genre:
            if char in Character[g]:
                counting[g] += 1
                break
        else:
            counting['미분류'] += 1

    # 캐릭터 수, 이름 순으로 정렬하기
    sortedl = sorted(counting.items(), key = lambda item : (-item[1], item[0]))
    result = [x[0] for x in sortedl]


    return result

N = int(input())
Name = input().split()
answer = solution(N, Name)

for i in answer:
    print(i)