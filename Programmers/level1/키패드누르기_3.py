# 키패드 누르기_3

def solution(numbers, hand):
    answer = ""

    #왼손과 오른손의 시작위치 초기화
    left_hand = 10 #10은 *을 뜻함
    right_hand = 11 #11은 #을 뜻함

    #distance[x][y] = 키패드x번과 키패드y번 사이의 거리
    distance = [[0, 4, 3, 4, 3, 2, 3, 2, 1, 2],
         [4, 0, 1, 2, 0, 2, 3, 0, 3, 4],
         [3, 1, 0, 1, 2, 1, 2, 3, 2, 3],
         [4, 2, 1, 0, 3, 2, 1, 4, 3, 2],
         [3, 0, 2, 3, 0, 1, 2, 0, 2, 3],
         [2, 2, 1, 2, 1, 0, 1, 2, 1, 2],
         [3, 3, 2, 1, 2, 1, 0, 3, 2, 1],
         [2, 0, 3, 4, 0, 2, 3, 0, 1, 2],
         [1, 3, 2, 3, 2, 1, 2, 1, 0, 1],
         [2, 4, 3, 2, 3, 2, 1, 2, 1, 0],
         [1, 0, 4, 5, 0, 3, 4, 0, 2, 3],
         [1, 5, 4, 0, 4, 3, 0, 3, 2, 0]]
    

    for num in numbers:
        if num in [1, 4, 7]:
            left_hand = num
            answer += "L"
        elif num in [3, 6, 9]:
            right_hand = num
            answer += "R"
        else:
            # 왼손이 더 가까이 있음
            if distance[left_hand][num] < distance[right_hand][num]:
                left_hand = num
                answer += "L"
            # 오른손이 더 가까이 있음
            elif distance[left_hand][num] > distance[right_hand][num]:
                right_hand = num
                answer += "R"
            # 왼손과 오른손의 거리가 같고 왼손잡이인 경우
            elif hand == "left":
                left_hand = num
                answer += "L"
            # 왼손과 오른손의 거리가 같고 오른손잡이인 경우
            else:
                right_hand = num
                answer += "R"
    return answer