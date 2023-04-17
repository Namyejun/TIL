## 정렬 알고리즘 비교 및 기초 문제 풀이

### 정렬 알고리즘 비교하기
- 앞서 다룬 네 가지 정렬 알고리즘을 비교하면 다음과 같다.
- 추가적으로 대부분의 프로그래밍 언어에서 지원하는 표준 정렬 라이브러리는 최악의 경우에도 `O(NlogN)`을 보장하도록 설계되어 있다.
- |정렬 알고리즘|평균 시간 복잡도|공간 복잡도|특징|
  |:---:|:---:|:---:|:---:|
  |선택 정렬|`O(N^2)`|`O(N)`|아이디어가 매우 간단하다.|
  |삽입 정렬|`O(N^2)`|`O(N)`|데이터가 거의 정렬되어 있을 때는 가장 빠르다.|
  |퀵 정렬|`O(NlogN)`|`O(N)`|대부분의 경우에 가장 적합하며, 충분히 빠르다.|
  |계수 정렬|`O(N + K)`|`O(N + K)`|데이터의 크기가 한정되어 있는 경우에만 사용이 가능하지만 매우 빠르게 동작한다.|

### <문제> 숫자 바꿔치기
``` python
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)
for i in range(K):
    if A[i] < B[i]:
        A[i] = B[i]
print(sum(A))
```
---

## 그래프 탐색의 기본, DFS와 BFS

### DFS(Depth-First Search)
- DFS는 깊이 우선 탐색이라고도 부르며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다.
- DFS는 스택 자료구조(혹은 재귀 함수)를 이용하며, 동작 과정은 다음과 같다.
    1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
    2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
    3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

### BFS(Breadth-First Search)
- BFS는 너비 우선 탐색이라고도 부르며 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘이다.
- BFS는 큐 자료구조를 이용하며, 동작 과정은 다음과 같다.
    1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
    2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리한다.
    3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

## 그래프 탐색 실습: DFS와 BFS 기초 문제 풀이

### <문제> 음료수 얼려먹기

``` python
from collections import deque
N, M = map(int, input().split())
ice = []
for i in range(N):
    ice.append(list(map(int, input().split())))
move = [(0,1),(1,0),(0,-1),(-1,0)]
visit = [[0 for i in range(M)] for j in range(N)]
cnt = 0

def bfs(n, m):
    x, y = n, m
    visit[x][y] = 1
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + move[i][0]
            ny = y + move[i][1]
            if 0 <= nx < N and 0 <= ny < M and ice[nx][ny] == 0 and visit[nx][ny] == 0:
                queue.append((nx, ny))
                visit[nx][ny] = 1
            else:
                continue
for i in range(N):
    for j in range(M):
        if ice[i][j] == 0 and visit[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt)
```

### <문제> 미로 탈출
``` python
from collections import deque
N, M = map(int, input().split())
maze = []
for i in range(N):
    maze.append(list(map(int, input().split())))
move = [(0,1),(1,0),(0,-1),(-1,0)]
path = [[0 for i in range(M)] for j in range(N)]

queue = deque()
queue.append((0, 0))
path[0][0] = 1
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + move[i][0], y + move[i][1]
        if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] != 0 and path[nx][ny] == 0:
            queue.append((nx, ny))
            path[nx][ny] = path[x][y] + 1
        else:
            continue
print(path[N-1][M-1])
```

---