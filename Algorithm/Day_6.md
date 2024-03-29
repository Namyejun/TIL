## 플로이드 워셜 알고리즘: 모든 출발지에서 다른 모든 출발지까지 최단 경로 계산

### 플로이드 워셜 알고리즘 개요
- 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산한다.
- 플로이드 워셜 알고리즘은 다익스트라 알고리즘과 마찬가지로 단계별로 거쳐가는 노드를 기준으로 알고리즘을 수행한다.
    - 다만 매 단계마다 방문하지 않는 노드 중에 최단 거리를 갖는 노드를 찾는 과정이 필요하지 않다.
    - 노드의 개수가 적은 상황에서 효과적으로 사용함. `O(N^3)`
- 플로이드 워셜은 2차원 테이블에 최단 거리 정보를 저장한다.
- 플로이드 워셜 알고리즘은 **다이나믹 프로그래밍 유형**에 속한다.

### 플로이드 워셜 알고리즘
- 각 단계마다 특정한 노드 k를 거쳐 가는 경우를 확인한다.
    - a에서 b로 가는 최단거리보다 a에서 k를 거쳐 b로 가는 거리가 더 짧은지 검사한다.
- 점화식
    - `D_ab = min(D_ab, D_ak + D_kb)`

- 성능 분석
    - 노드의 개수가 N개일 때 알고리즘상으로 N번의 단계를 수행한다.
        - 각 단계마다 `O(N^2)`의 연산을 통해 현재 노드를 거쳐 가는 모든 경로를 고려한다.
    - 따라서 플로이드 워셜 알고리즘의 총 시간 복잡도는 `O(N^3)`이다.

- 플로이드 워셜을 사용하는 경우는 노드의 개수가 500개 이하인 경우가 많다.
    - 이마저도 125,000,000 1억이 넘기에 시간 제한이 넉넉하지 않다면 시간초과가 난다.

---