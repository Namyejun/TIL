## 크루스칼 알고리즘: 최소 신장 트리를 찾는 알고리즘

### 신장 트리(Spanning Tree)
- 그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
- 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건은 트리의 조건이기도 하다.

### 최소 신장 트리(Minimum Spanning Tree)
- 최소한의 비용으로 구성되는 신장 트리\

### 크루스칼 알고리즘
- 대표적인 최소 신장 트리 알고리즘
- 그리디 알고리즘으로 분류된다.
- 동작과정
1. 간선 데이터를 비용에 따라 오름차순 정렬
2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
   
   (유니온 파인드 자료구조)
   1. 사이클이 발생하지 않는 경우 포함
   2. 발생하는 경우 미포함
3. 모든 간선에 대해 2번의 과정 반복

- 성능 분석
    - 크루스칼 알고리즘은 간선의 개수가 E일 때, `O(ElogE)`의 시간 복잡도를 가진다.
    - 크루스칼 알고리즘에서 가장 많은 시간을 요구하는 곳은 간선의 정렬 부분이다.
        - 표준 라이브러리를 이용해 정렬할 시 시간 복잡도가 `O(ElogE)`이다.

---

## 최소 공통 조상: 트리에서의 최소 공통 조상을 찾는 알고리즘

### 최소 공통 조상(Lowest Common Ancestor)
- [백준 11437번 문제](https://www.acmicpc.net/problem/11437)
``` python
import sys
sys.setrecursionlimit(100000)
def dfs(x, t):
    check[x] = 1
    depth[x] = t
    for near in graph[x]:
        if not check[near]:
            parent[near][0] = x
            dfs(near, t+1)

def set_parent():
    dfs(1, 1)
    for i in range(1, 16):
        for j in range(1, N + 1):
            if parent[j][i] == 0:
                parent[j][i] = parent[parent[j][i-1]][i-1]

def LCA(a, b):
    if depth[a] > depth[b]:
        a, b = b, a
    for i in range(15, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            b = parent[b][i]
    if a == b:
        return a
    else:
        for i in range(15, -1, -1):
            if parent[a][i] != parent[b][i]:
                a = parent[a][i]
                b = parent[b][i]
        return parent[a][i]
    
N = int(input())
graph = [[] for i in range(N + 1)]
check = [0 for i in range(N + 1)]
depth = [0 for i in range(N + 1)]
parent = [[0]*16 for i in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
set_parent()
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(LCA(a, b))
```
- 최소 공통 조상(LCA) 문제는 두 노드의 공통된 조상 중에서 가장 가까운 조상을 찾는 문제이다.

### 기본적인 최소 공통 조상(LCA) 알고리즘
1. 모든 노드에 대한 깊이(depth)를 계산한다.
2. 최소 공통 조상을 찾을 두 노드를 확인한다.
   1. 먼저 두 노드의 깊이가 동일하도록 거슬러 올라간다.
   2. 이후에 부모가 같아질 때까지 반복적으로 두 노드의 부모 방향으로 거슬로 올라간다.
3. 모든 LCA(a, b) 연산에 대해 2번의 과정을 반복한다.

- 성능 분석
    - 매 쿼리마다 부모 방향으로 거슬로 올라가기 위해 최악의 경우 `O(N)`의 시간 복잡도가 요구된다.
        - 따라서 모든 쿼리를 처리할 때의 시간 복잡도는 `O(NM)`이다.

### 최소 공통 조상(LCA) 알고리즘 개선하기
- 각 노드가 거슬러 올라가는 속도를 빠르게 만드는 방법
    - 2의 제곱 형태로 거슬러 올라가도록 하면 O(logN)의 시간 복잡도를 보장할 수 있다.
    - 메모리를 조금 더 사용하여 각 노드에 대해 2^i번째 부모에 대한 정보를 기록한다.
    - 모든 노드에 대해 깊이와 2^i번째 부모에 대한 정보를 계산한다.
    - 2^i번째 부모에 대한 정보는 다이나믹 프로그래밍을 이용해 구할 수 있다.

### 개선된 최소 공통 조상(LCA) 알고리즘: 시간 복잡도 분석
- 다이나믹 프로그래밍을 이용해 시간 복잡도 개선
    - `parent[j][i] = parent[parent[j][i-1]][i-1]`
        - j번째 노드의 2^i번째 부모는 j번째 노드의 2^(i-1)번째 부모의 2^(i-1)번째 부모이다.
        - `2^i = 2^(i-1) + 2^(i-1) `이므로
    - 세그먼트 트리를 이용하는 방법도 존재한다.
- 매 쿼리마다 부모를 거슬러 올라가기 위해서는 `O(logN)`의 복잡도가 필요하다.
    - 따라서 모든 쿼리를 처리할 때 `O(MlogN)`의 시간 복잡도가 필요하다.

---