
n, m = map(int, input().split())
heights = [0] + list(map(int, input().split()))
rained_area = set()

# 장마기간동안 물 높이 처리 
for day in range(1, m+1):
	
	#장마 day일째 s~e번까지 비
	s,e = map(int, input().split())
	#day일째 s~e번째 집 물높이+1
	for i in range(s, e+1):
		heights[i] += 1
		rained_area.add(i)
	
	#배수시스템 처리
	if day%3==0:	
		#비가 내렸던 지역 물높이 -1
		for area in rained_area:
			heights[area] -= 1
		
		#초기화
		rained_area = set()

	
# 결과 출력
print(' '.join(map(str, heights[1:])))
	
	
	