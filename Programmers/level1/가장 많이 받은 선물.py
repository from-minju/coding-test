def solution(friends, gifts):
    # 친구들의 전체 수
    num = len(friends)

    # 주고받은 선물 표
    giveAndTake = [[0 for _ in range(num)] for _ in range(num)]
    # 선물지수 표 [준 선물,	받은 선물, 선물 지수]
    giftData = [[0 for _ in range(3)] for _ in range(num)]
    # 다음달 받을 선물의 수 표
    nextMonthGift = [[0 for _ in range(num)] for _ in range(num)]

    # 1. 주고 받은 선물 표 만들기 : giveAndTake
    for str in gifts:
        # a:선물 준 사람, b:선물 받은 사람
        a, b = str.split(' ')
        aIdx = friends.index(a)
        bIdx = friends.index(b)
        giveAndTake[aIdx][bIdx] += 1
        
    # 2. 선물지수 표 만들기 : giftData
        giftData[aIdx][0] += 1 # 준 선물 개수 처리
        giftData[bIdx][1] += 1 # 받은 선물 개수 처리
        # a,b의 선물지수 계산 업데이트
        giftData[aIdx][2] = giftData[aIdx][0] - giftData[aIdx][1]
        giftData[bIdx][2] = giftData[bIdx][0] - giftData[bIdx][1]

    # 3. 다음달 받을 선물 수 표 만들기
    for me in range(num): #나
        for you in range(num): #상대방
            if(me == you): continue
            
            # me가 you에게 준 선물의 수 
            gave = giveAndTake[me][you]
            # me가 you에게 받은 선물의 수 
            received = giveAndTake[you][me]

            if gave > received:
                nextMonthGift[me][you] += 1
            # elif gave < received:
            #     nextMonthGift[you][me] += 1
            elif(gave == received): # 주고받은 선물의 수가 같거나 기록이 없는 경우
                myGiftData = giftData[me][2] #나의 선물지수
                yourGiftData = giftData[you][2] #상대방의 선물지수
                if myGiftData > yourGiftData:
                    nextMonthGift[me][you] += 1
                # elif myGiftData < yourGiftData:
                #     nextMonthGift[you][me] += 1
    
    # 4. 다음달 가장 많이 받는 선물 수 계산하여 리턴하기
    numOfNextMonthGift = [0 for _ in range(num)]
    for idx in range(num):
        numOfNextMonthGift.append(sum(nextMonthGift[idx]))
    numOfNextMonthGift.sort(reverse=True)

    return numOfNextMonthGift[0]

    # print(giveAndTake)
    # print(giftData)
    # print(nextMonthGift)

friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

print(solution(friends, gifts))