# BFS (Breadth First Search) 너비 우선 탐색
# 가까운 노드부터 탐색하는 알고리즘

#1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
#2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리를 한다.
#3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.


from collections import deque

# BFS 함수 정의
def bfs(graph, start, visited):
    
    queue = deque([start]) #큐 초기화
    visited[start] = True

    while queue:
      v = queue.popleft()
      print(v, end=' ')

      for i in graph[v]:
          if not visited[i] : #방문하지 않은 노드라면
              queue.append(i)
              visited[i] = True
            

    
# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)

#결과 : 1 2 3 8 7 4 5 6 